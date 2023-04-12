import sys
import os
import ctypes
import pickle
import shutil
import time
from PySide6.QtCore import QThread, Signal
# from PyQt5.Qt import QThread
# from PyQt5.QtCore import pyqtSignal



# c盘根目录临时文件夹名
root_tmp_dir = "C:/_$backuptool_$zip_$tmp_$dir_/"

# 判断文件路径是否以“C:/”开头而且仅有一个“/”字符
def is_root(path: str) -> bool:
    ret = False
    if path.startswith("C:/") and path.find("/") == path.rfind("/"):
        ret = True
    return ret


# 给根目录下的文件名加入临时路径
def add_tmp_path(path: str) -> str:
    return path.replace("C:/", root_tmp_dir)


# 删除失败的备份目录
def del_backup_dir(backup_dest_path:str):
    if os.path.isdir(backup_dest_path):
        try:
            shutil.rmtree(backup_dest_path)
        except:
            pass


# 读取设置并返回数据
def load_setting() -> object:
    try:
        with open(res_path(File.CURRENT_SETTING_FILENAME), "rb") as f:
            f_read = pickle.load(f)
            setting = f_read
            f.close()
            return setting
    except:
        return None

# 保存设置到默认文件夹
def save_setting(setting:object):
    try:
        with open(res_path(File.CURRENT_SETTING_FILENAME), "wb") as f:
            pickle.dump(setting, f)
            f.close()
    except:
        pass


# 去除路径名前缀
def cut_pathname_prefix(filename:str) -> str:
    # Windows系统,替换":\"为"盘\"
    if sys.platform == "win32":
        filename = filename.replace(u":\\", "盘\\")
    # 其他系统,截掉"/Volumes/",去掉首个"/"
    else:
        if filename.startswith("/Volumes/"):
            filename = filename[9:]
        if filename.startswith("/"):
            filename = filename[1:]
    return filename


# 返回经过处理资源相对路径后的文件路径
def res_path(filename:str) -> str:
    if sys.platform == "win32":
        mydoc_path = os.path.expanduser("~\Documents\BackupTool")
        if not os.path.exists(mydoc_path):
            os.makedirs(mydoc_path)
        return os.path.join(mydoc_path, filename)
    else:
        relative_path = "../Resources"
        path = os.path.join(os.path.dirname(sys.argv[0]), relative_path)
        return os.path.join(path, filename)


# 判断是否空间不足，正常返回0
# 空间小于100MB返回-1,获取空间失败返回-2,其他未知错误返回-99
def insufficient_space(dst_drive:str, needsizeMB:float) -> int:
    ret:int = -9
    # 获取目标文件夹剩余空间，单位MB
    freespaceMB = 0.0
    try:
        # Windows系统
        if sys.platform == "win32":
            free_bytes = ctypes.c_ulonglong(0)
            ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dst_drive), None, None, ctypes.pointer(free_bytes))
            freespaceMB = free_bytes.value / 1024 / 1024
        # 其他系统
        else:
            stat = os.statvfs(dst_drive)
            freespaceMB =  stat.f_bavail * stat.f_frsize / 1024 / 1024
        # 如果剩余空间不足100MB
        if (freespaceMB - needsizeMB) < 100:
            ret = -1
        else:
            ret = 0
    except Exception as e:
        ret = -2
    return ret

# 本类集合文件操作相关方法
class File(QThread):

    # 定义信号槽
    copied_signal = Signal(bool)
    copy_err_signal = Signal(str)
    # 参数由此变量传入
    args = ()
    # c盘根目录临时文件夹名
    root_tmp_dir = "C:/_$backuptool_$zip_$tmp_$dir_"

    # 默认设置文件名
    CURRENT_SETTING_FILENAME = "backup.setting"

    # QThread入口
    def run(self):
        self.copy_file(self.args[1], self.args[2], self.args[3])

    # 复制文件
    def copy_file(self, srcfile:str, dstfile:str, dstpath:str):
        # 判断源文件是否存在
        if not os.path.isfile(srcfile):
            self.copy_err_signal.emit("Source file not exist")
        else:
            # 分离文件名和路径
            dpath, dname = os.path.split(dstfile)
            # 如果目的文件夹不存在则创建之
            if not os.path.exists(dpath):
                try:
                    os.makedirs(dpath)
                except OSError as e:
                    self.copy_err_signal.emit(e)
            # 复制文件
            try:
                shutil.copy(srcfile, dstfile)
            except Exception as e:
                self.copy_err_signal.emit(e)
        # 如果文件复制完毕，发送信号
        while not os.path.isfile(dstfile):
            time.sleep(0.5)
        else:
            self.copied_signal.emit(True)