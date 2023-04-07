import sys
import os
import shutil
import time
import datetime
import zipfile
import logging
from PyQt5 import Qt, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox, QMenu
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
# 导入项目内模块
import ui_backing, ui_finish, ui_editlist
from bks_file_opration import *
from global_dict import GlobalDict

# 日志
class Logger:
    # log文件名
    LOG_FILE = res_path("backup.log")
    # 设置logger
    logger = logging.getLogger()
    logger.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    # 设置输出到文件
    handler = logging.FileHandler(LOG_FILE, mode='w')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    # 设置输出到控制台
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger.addHandler(console)


# 保存设置变量
class Setting:

    # 用户选择的备份目的文件夹
    __target:str = ""
    # 最近打开的文件夹
    __lastdir:str = ""
    # 生成的时间戳名字
    __timestamp:str = ""
    # 文件及压缩状态{文件/文件夹名:压缩标识}
    __data:dict = {}
    # logger
    logger = Logger.logger

    def __init__(self):
        self.init_setting()

    def init_setting(self):
        self.__data= {}
        self.__target = ""

    def get_data(self) -> dict:
        return self.__data

    def set_data(self,data:dict):
        self.__data = data

    def get_target(self) -> str:
        return self.__target

    def set_target(self, t:str):
        self.__target = t

    def get_lastdir(self) -> str:
        return self.__lastdir

    def set_lastdir(self, path:str):
        self.__lastdir = path

    def get_timestamp(self) -> str:
        return self.__timestamp

    def set_timestamp(self, timestamp:str):
        self.__timestamp = timestamp

    # 用property定义为属性
    Data = property(get_data, set_data)
    Target = property(get_target, set_target)
    Lastdir = property(get_lastdir, set_lastdir)
    Timestamp = property(get_timestamp, set_timestamp)

    # dict{item:compress,..} 转 QStandardItemModel
    def dict_to_data(self, dic:dict, model:QStandardItemModel) -> QStandardItemModel:
        model.clear()
        items = list(dic.items())
        for i in range(len(items)):
            model.appendRow(QStandardItem(str(items[i][0])))
            for j in range(len(items[i])):
                model.setItem(i, j, QStandardItem(str(items[i][j])))
        return model

    # QStandardItemModel 转 dict{item:compress,..}
    def data_to_dict(self, model:QStandardItemModel) -> dict:
        ret_list = []
        for row in range(model.rowCount()):
            tmp_list = []
            for col in range(model.columnCount()):
                tmp_list.append(model.item(row, col).text())
            ret_list.append(tuple(tmp_list))
        return dict(ret_list)

    # 线性列表转元组列表矩阵,l_list=线性列表,part_num=每组的成员数量
    def linear_to_matrix(self, l_list:list, part_num:int) -> list:
        ret_list = []
        for i in range(int(len(l_list) / part_num)):
            if len(l_list) > part_num:
                ret_list.append(tuple(l_list[:part_num]))
                l_list = l_list[part_num:]
        ret_list.append(tuple(l_list))
        return ret_list


# 新建备份/管理备份的GUI部件与业务逻辑
class EditListWidget(ui_editlist.Ui_Form, QWidget):
    # 最小窗口大小
    min_window_width:int = 500
    min_window_height:int = 235
    # 根据窗口宽度计算列宽偏移量
    column_width_offset:int = 184

    # 采集拖放文件名的临时变量
    tmp_dorp_filename:list = []

    # 设置界面
    def setup_action(self):
        # 设置窗口无标题栏，透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(560, 316)
        if not sys.platform == "win32":
            font = QFont()
            font.setFamily("Microsoft YaHei")
            font.setPointSize(12)
            self.lab_path_name.setFont(font)
            self.tableView.setFont(font)
            self.close_frame_verticalLayout.setContentsMargins(26, 6, 16, 30)
            self.btns_verticalLayout.setContentsMargins(20, -1, 10, -1)

        # tableview模型绑定
        self.load_setting()
        self.f_model = QStandardItemModel(1,2)
        self.tableView.setModel(self.f_model)

        # 刷新显示
        self.renovate_info()
        # 设置窗口title
        if SETTING.Data:
            self.setWindowTitle("上次备份了以下文件")
        else:
            self.setWindowTitle("请选择目的文件夹和要备份的文件")
        # 设置按钮点击事件
        self.btn_start_backup.clicked.connect(lambda : self.start_clicked())
        self.btn_set_target.clicked.connect(lambda : self.set_target_clicked())
        self.btn_clear_file.clicked.connect(lambda : self.clear_file_clicked())
        self.btn_close.clicked.connect(lambda : self.close_clicked())
        # 打开窗体drop
        self.setAcceptDrops(True)
        # 设置右键菜单
        self.tableView.customContextMenuRequested.connect(self.right_menu)

    # 读取保存在外部的设置
    def load_setting(self):
        s = load_setting()
        if s:
            SETTING.Data = s.Data
            SETTING.Target = s.Target
            SETTING.Lastdir = s.Lastdir
            SETTING.logger.info("已读取设置文件")
        else:
            SETTING.logger.info("读取设置失败")

    # QWidget关闭事件，清除所有窗口实例，退出到系统
    def closeEvent(self, event):
        for w in QApplication.instance().allWidgets():
            if w != self:
                del w
        event.accept()
        self.close()

    # 鼠标按下事件
    def mousePressEvent(self, event):
        # 获取窗体当前坐标
        self.origin_x = self.x()
        self.origin_y = self.y()
        # 获取鼠标点击坐标
        self.mouse_x = event.globalX()
        self.mouse_y = event.globalY()
        # 如果按住右下角
        if self.childAt(event.x(), event.y()) in [self.conner_frame]:
            self.drag_event = 1
        # 如果按住右边框
        elif self.childAt(event.x(), event.y()) in [self.right_side_frame]:
            self.drag_event = 2
        # 如果按住下边框
        elif self.childAt(event.x(), event.y()) in [self.bottom_side_frame]:
            self.drag_event = 3
        # 只移动不调整大小
        else:
            self.drag_event = 0
            super(EditListWidget, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()


    # 鼠标弹起事件
    def mouseReleaseEvent(self, event):
        self.origin_x = None
        self.origin_y = None
        self.start_x = None
        self.start_y = None
        self.mouse_x = None
        self.mouse_y = None
        # 调整列宽
        self.tableView.setColumnWidth(0, self.width() - self.column_width_offset)

    # 鼠标按住拖动事件
    def mouseMoveEvent(self, event):
        # 只移动
        if self.drag_event == 0:
            super(EditListWidget, self).mouseMoveEvent(event)
            dis_x = event.x() - self.start_x
            dis_y = event.y() - self.start_y
            self.move(self.x() + dis_x, self.y() + dis_y)
        # 调整宽和高
        elif self.drag_event == 1:
            if event.x() < self.min_window_width:
                x = self.min_window_width
            else:
                x = event.x()
            if event.y() < self.min_window_height:
                y = self.min_window_height
            else:
                y = event.y()
            self.setGeometry(self.origin_x, self.origin_y, x, y)
            self.frame.setGeometry(0, 0, x, y)
            # 调整列宽
            self.tableView.setColumnWidth(0, self.width() - self.column_width_offset)

        # 只调整宽
        elif self.drag_event == 2:
            if event.x() < self.min_window_width:
                x = self.min_window_width
            else:
                x = event.x()
            self.setGeometry(self.origin_x, self.origin_y, x, self.height())
            self.frame.setGeometry(0, 0, x, self.frame.height())
            # 调整列宽
            self.tableView.setColumnWidth(0, self.width() - self.column_width_offset)
        # 只调整高
        elif self.drag_event == 3:
            if event.y() < self.min_window_height:
                y = self.min_window_height
            else:
                y = event.y()
            self.setGeometry(self.origin_x, self.origin_y, self.width(), y)
            self.frame.setGeometry(0, 0, self.frame.width(), y)


    # 获取tableView中的选中项目
    def get_selected(self) -> dict:
        # 如果数据库不是空的
        if SETTING.Data:
            # 收集选中的条目
            s = self.tableView.selectedIndexes()
            tmp_list = []
            for i in s:
                tmp_list.append(self.tableView.model().index(i.row(), i.column()).data())
            if tmp_list:
                # 两个值为一组元组，转为字典
                ret_dict = dict(SETTING.linear_to_matrix(tmp_list, 2))
                SETTING.logger.info(f"选中 {ret_dict}")
                return ret_dict

        else:
            return {}

    # 拖放文件进入窗体事件
    def dragEnterEvent(self, event):
        tmp_list = event.mimeData().text().splitlines()
        for item in tmp_list:
            # 记录文件名
            if sys.platform == "win32":
                self.tmp_dorp_filename.append(item[8:])
            else:
                self.tmp_dorp_filename.append(item[7:])
        event.accept()

    # 拖放文件鼠标按键松开事件
    def dropEvent(self, event):
        if self.tmp_dorp_filename:
            for item in self.tmp_dorp_filename:
                # 如果是文件夹，后面加*.*
                if os.path.isdir(item):
                    if sys.platform == "win32":
                        item = item + "/*.*"
                    else:
                        item = item + "*.*"
                # 添加文件名到列表
                SETTING.Data.update({item:""})
                SETTING.logger.info(f"拖放添加 {item}")
            self.tmp_dorp_filename = []
            self.renovate_info()

    # 创建右键菜单
    def right_menu(self, point):
        # 获取选中项
        selected_items = self.get_selected()
        # 如果是空的，什么都不做
        if not selected_items:
            return
        # 定义右键菜单
        r_menu = QMenu(self.tableView)
        screenPos = self.tableView.mapToGlobal(point)
        # 如果仅有一个选择项
        if len(selected_items)==1:
            if "压缩" in selected_items.values():
                del_items = r_menu.addAction("移除")
                uncomprs_item = r_menu.addAction("取消压缩")
                click = r_menu.exec_(screenPos)
                if click == uncomprs_item:
                    self.set_item_uncompress(list(selected_items.keys()))
                elif click == del_items:
                    self.del_items(selected_items)
            else:
                del_items = r_menu.addAction("移除")
                comprs_item = r_menu.addAction("备份时压缩")
                click = r_menu.exec_(screenPos)
                if click == comprs_item:
                    self.set_item_compress(list(selected_items.keys()))
                elif click == del_items:
                    self.del_items(selected_items)
        # 如果有多个选择项
        elif len(selected_items) > 1:
            del_items = r_menu.addAction("移除选中项")
            if "" in list(selected_items.values()):
                compress_items = r_menu.addAction("备份时压缩选中项")
            if "压缩" in list(selected_items.values()):
                uncompress_items = r_menu.addAction("取消选中项压缩")
            click = r_menu.exec_(screenPos)
            if click == del_items:
                self.del_items(selected_items)
            try:
                if click == compress_items:
                    self.set_item_compress(list(selected_items.keys()))
            except:
                pass
            try:
                if click == uncompress_items:
                    self.set_item_uncompress(list(selected_items.keys()))
            except:
                pass

    # 开始备份按钮的点击事件
    def start_clicked(self):
        if SETTING.Data and SETTING.Target:
            # 保存设置
            save_setting(SETTING)
            SETTING.logger.info("已保存设置")
            self.close()
            SETTING.logger.info("开始备份")
            backing_window.show_backing()
        else:
            self.show_message("请先设置目的文件夹以及备份文件")

    # close按钮点击事件
    def close_clicked(self):
        SETTING.logger.info("关闭窗口")
        self.close()
        ExitProgram.exit(0)

    # 选择目的文件夹对话框
    def set_target_clicked(self):
        dir_name = QFileDialog.getExistingDirectory(self, "请选择备份目的文件夹", os.path.expanduser("~/"))
        if dir_name:
            SETTING.logger.info(f"设置备份目的文件夹 {dir_name}")
            SETTING.Target = dir_name
        self.renovate_info()

    # 设置压缩状态
    def set_item_compress(self,items:list):
        for i in items:
            if SETTING.Data[i] == "":
                SETTING.Data[i] = "压缩"
                SETTING.logger.info(f"{i} 设置为<压缩>")
        self.renovate_info()

    # 取消压缩状态
    def set_item_uncompress(self,items:list):
        for i in items:
            if SETTING.Data[i] == "压缩":
                SETTING.Data[i] = ""
                SETTING.logger.info(f"{i} 取消<压缩>")
        self.renovate_info()

    # 清除选中的项目
    def del_items(self,items:dict):
        del_list = []
        # 显示的内容只保留文件名
        list_str = ""
        for i in list(items.keys()):
            path_str, add_str = os.path.split(i)
            if not i.endswith("*.*"):
                list_str = list_str + "\n'" + add_str + "'"
            else:
                tmp_str = (os.path.dirname(i))
                tmp_str = tmp_str[tmp_str.rfind("/")+1:]
                list_str = list_str + "\n'" + tmp_str + "/*.*'"
            del_list.append(i)
        # 显示移除文件弹窗
        if self.show_message("确定把以下文件/文件夹从列表移除吗？"+list_str, delitem = items):
            self.del_from_list(del_list)

    # 清空列表按钮点击事件
    def clear_file_clicked(self):
        SETTING.logger.info("从列表清除所有文件")
        SETTING.Data = {}
        self.renovate_info()

    # 从列表中去除文件
    def del_from_list(self, del_list:list):
        for i in del_list:
            SETTING.logger.info(f"{SETTING.Data[i]} 从列表中移除")
            del SETTING.Data[i]
        self.renovate_info()

    # 刷新显示信息
    def renovate_info(self):

        help_dict = {"点击上方「备份到」按钮，选择备份目的文件夹，":"",
                    "然后把要备份的文件/文件夹拖到这里。":"",
                    "选中一个或多个条目，点击鼠标右键，有更多选项，":"",
                    "可以设置是否压缩，以及是否从列表移除。":"",
                    "设置完毕后，点「开始备份」按钮，":"",
                    "将在备份目的文件夹下建立新的备份文件夹，以当前时间命名。":"",
                     "只要备份过一次，后面都会记住列表的内容设置。": "",
                    "--> 开始吧！":"",
                     }

        # 如果全部SETTING是空的，表示首次运行，显示帮助信息
        if (not SETTING.Data) and (not SETTING.Target) and (
                not SETTING.Lastdir) and (not SETTING.Timestamp):
            self.f_model = SETTING.dict_to_data(help_dict,self.f_model)
        else:
            self.f_model = SETTING.dict_to_data(SETTING.Data,self.f_model)
        self.lab_path_name.setText("   " + SETTING.Target)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.horizontalHeader().setVisible(False)
        # 调整列宽
        self.tableView.setColumnWidth(0, self.width() - self.column_width_offset)
        self.tableView.setColumnWidth(1, 60)


    # 弹窗消息框
    def show_message(self, msg:str, delitem:dict = {}) -> bool:
        # 如果带参数
        if delitem:
            msg_box = QMessageBox.warning(self, "警告", msg,
                                          QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            # 如果点yes，返回True将执行后续操作
            if msg_box==QMessageBox.Yes:
                return True
        # 不带参数，弹出普通消息框，返回False
        else:
            QMessageBox.warning(self, "警告", msg, QMessageBox.Ok)
            return False


# 进度条窗口的GUI部件与业务逻辑
class BackingWidget(ui_backing.Ui_Form, QWidget, Qt.QThread):

    # 点击取消按钮的信号槽，通知后台中断文件操作
    cancel_signal = QtCore.pyqtSignal(bool)
    # zip列表
    zip_file_list:list = []
    # zip临时文件后缀
    zip_tmpfile_suffix:str = "._backuptool_tmp_zipfile"
    # 压缩中产生的源文件夹zip临时文件表
    src_zip_tmp_files:list = []
    # 进度条rate值
    progressbar_rate:int = 1
    # 进度条阈值
    progressbar_threshold:int = 1


    # 设置界面
    def setup_action(self):
        # 设置窗口无标题栏，透明，置顶
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        # 非Windows版UI调整
        if not sys.platform == "win32":
            font = QFont()
            font.setFamily("Microsoft YaHei")
            font.setPointSize(12)
            self.label.setFont(font)
        # 设置按钮事件
        self.btn_cancel.clicked.connect(lambda : self.cancel_clicked())
        # 设置本次备份的子文件夹名
        time_stamp = datetime.datetime.now().strftime("%Y")
        time_stamp = time_stamp + "年" + datetime.datetime.now().strftime("%m")
        time_stamp = time_stamp + "月" + datetime.datetime.now().strftime("%d")
        time_stamp = time_stamp + "日" + datetime.datetime.now().strftime("%H.%M.%S")
        SETTING.Timestamp = time_stamp
        self.backup_dest_path = SETTING.Target + "/Backup@" + SETTING.Timestamp

        # 检查原始文件和目标硬盘目录是否存在
        check_files_err = []
        for item in SETTING.Data.keys():
            if item.endswith("*.*"):
                if not os.path.isdir(os.path.dirname(item)):
                    check_files_err.append(item)
            elif not os.path.isfile(item):
                check_files_err.append(item)
        if check_files_err:
            err_msg = "\n".join(check_files_err)
            err_msg = "找不到" + err_msg
            SETTING.logger.error(err_msg)
            self.exit_show_message(err_msg)
        if sys.platform == "win32":
            dst_drive, _ = os.path.splitdrive(self.backup_dest_path)
        else:
            dst_drive = SETTING.Target
        if os.path.isdir(dst_drive):
            try:
                os.mkdir(self.backup_dest_path)
            except OSError as e:
                SETTING.logger.error(e)
                self.exit_show_message("目标磁盘创建文件夹失败，请检查用户权限")
        else:
            SETTING.logger.error(f"找不到磁盘{dst_drive}")
            self.exit_show_message(f"找不到磁盘{dst_drive}")

        # 分拣文件得到待拷贝文件表，待压缩文件放在self.zip_file_list
        to_copy_filelist = self.sortout_filelist()
        # 计算各源磁盘待压缩文件的大小
        every_src_drv_for_zip = {}
        for item in self.zip_file_list:
            filesizeMB = 0.0
            if sys.platform == "win32":
                drv, _ = os.path.splitdrive(item)
            else:
                drv = item[:item.find("/", item.find("/", item.find("/") + 1) + 1)]
            #是文件夹
            if os.path.isdir(item):
                for paths, dirnames, filenames in os.walk(item):
                    for f in filenames:
                        filesizeMB += os.stat(paths + "/" + f).st_size / 1024 / 1024
            else:
                filesizeMB += os.stat(item).st_size / 1024 / 1024
            every_src_drv_for_zip[drv] = float(every_src_drv_for_zip.get(drv, "0")) + filesizeMB
        # 比较各源磁盘空间
        for dst_drive in list(every_src_drv_for_zip.keys()):
            needsizeMB = float(every_src_drv_for_zip[dst_drive])
            try:
                # Windows系统
                if sys.platform == "win32":
                    free_bytes = ctypes.c_ulonglong(0)
                    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dst_drive), None, None,
                                                               ctypes.pointer(free_bytes))
                    freespaceMB = free_bytes.value / 1024 / 1024
                # 其他系统
                else:
                    stat = os.statvfs(dst_drive)
                    freespaceMB = stat.f_bavail * stat.f_frsize / 1024 / 1024
                # 如果剩余空间不足100MB
                if (freespaceMB - needsizeMB) < 100:
                    self.exit_show_message(f"{dst_drive}磁盘空间不足，无法压缩文件。")
                    SETTING.logger.error(f"{dst_drive}磁盘空间不足，无法压缩文件。")
            except Exception as e:
                self.exit_show_message(f"{dst_drive}磁盘错误")
                SETTING.logger.error(e)
        # 设置复制文件线程
        self.backing_up_files = BackingUpFiles()
        # 设置信号槽
        self.backing_up_files.filename_signal.connect(self.set_label_text)
        self.backing_up_files.rate_signal.connect(self.set_progressbar_rate)
        self.backing_up_files.finish_signal.connect(self.copy_finish)
        self.backing_up_files.copy_err_signal.connect(self.copy_error)
        # 传参数
        self.backing_up_files.to_copy_list = to_copy_filelist
        # 如果有压缩任务
        if self.zip_file_list:
            # 设置压缩文件线程
            self.zip_files = ZipFiles()
            # 设置信号槽
            self.zip_files.zipping_signal.connect(self.set_zip_text)
            self.zip_files.ziprate_signal.connect(self.set_zip_progress)
            self.zip_files.zipfinish_signal.connect(self.zip_finish_and_start_copy)
            # 传参数
            self.zip_files.zip_file_list = self.zip_file_list
            self.zip_files.zip_tmpfile_suffix = self.zip_tmpfile_suffix
            # 压缩线程开始工作
            self.zip_files.start()
        else:
            # 复制文件线程开始工作
            self.backing_up_files.start()
        # 设置timer，显示压缩进度条用
        self.rate_timer = QtCore.QBasicTimer()


    # 拖动窗口鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(BackingWidget, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    # 拖动窗口鼠标弹起事件
    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    # 拖动窗口鼠标按住拖动事件
    def mouseMoveEvent(self, event):
        super(BackingWidget, self).mouseMoveEvent(event)
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)

    # QThread入口
    def run(self):
        self.setup_action()

    # 压缩完毕信号槽接收函数
    def zip_finish_and_start_copy(self, ziped_file_list:list):
        self.rate_timer.stop()
        # 信号槽接收到的zip文件列表保存到本地
        self.src_zip_tmp_files = ziped_file_list
        # 开始复制文件子线程
        self.backing_up_files.start()

    # 分拣文件
    # 有压缩标记的文件/文件夹，在总列表中替换名称为临时zip文件名，加入待压缩列表，
    # 没有压缩标记的文件夹，提取子文件夹里的文件名，插入到列表
    def sortout_filelist(self) -> list:
        # 处理列表中的文件夹
        to_copy_list = list(SETTING.Data.keys())
        for item in to_copy_list:
            # 如果是压缩tag
            if SETTING.Data[item] == "压缩":
                if item.endswith("*.*"):
                    parent_path = os.path.dirname(item)
                    # 文件夹添加到zip表
                    self.zip_file_list.append(parent_path)
                    tmp_zip_filename = [parent_path + self.zip_tmpfile_suffix]
                    if not os.path.isdir(parent_path):
                        msg = f"找不到{parent_path}文件夹，请检查是否存在。"
                        self.exit_show_message(msg)
                    # 如果位于C盘根目录，添加zip临时文件夹路径
                    elif is_root(parent_path):
                        tmp_zip_filename = [add_tmp_path(tmp_zip_filename[0])]
                else:
                    # 文件添加到zip表
                    self.zip_file_list.append(item)
                    tmp_zip_filename = [item + self.zip_tmpfile_suffix]

                    if not os.path.isfile(item):
                        msg = f"找不到{item}，请检查文件是否存在。"
                        self.exit_show_message(msg)
                    # 如果位于C盘根目录，添加zip临时文件夹路径
                    elif is_root(item):
                        tmp_zip_filename = [add_tmp_path(tmp_zip_filename[0])]
                # 总表替换临时文件名
                front_half = to_copy_list[:to_copy_list.index(item)]
                lower_half = to_copy_list[to_copy_list.index(item) + 1:]
                to_copy_list = front_half + tmp_zip_filename + lower_half
                continue
            # 如果item不是以文件存在
            if not os.path.isfile(item):
                # 如果item以*.*结尾，表示这是个文件夹
                if item.endswith("*.*"):
                    # 如果文件夹存在
                    parent_path = os.path.dirname(item)
                    if os.path.isdir(parent_path):
                        # 去掉*.*
                        dir_name = parent_path
                        # 遍历子文件夹里的所有文件到列表
                        in_dir_files = []
                        for paths, dirnames, filenames in os.walk(dir_name):
                            for file in filenames:
                                fullfilename = os.path.join(paths, file)
                                in_dir_files += [fullfilename, ]
                        # 将子文件夹内文件列表插入到列表
                        front_half = to_copy_list[:to_copy_list.index(item)]
                        lower_half = to_copy_list[to_copy_list.index(item) + 1:]
                        to_copy_list = front_half + in_dir_files + lower_half
                    else:
                        # 弹窗，显示找不到文件夹，退出
                        msg = f"找不到{parent_path}文件夹，请检查是否存在。"
                        self.exit_show_message(msg)
                else:
                    # 弹窗，显示找不到文件，退出
                    msg = f"找不到{item}，请检查文件是否存在。"
                    self.exit_show_message(msg)
        return  to_copy_list

    # 设置进度条的文字
    def set_label_text(self, filename:str):
        self.label.setText("正在备份 " + filename)
        SETTING.logger.info("复制 " + filename)

    # 设置进度条的进度值
    def set_progressbar_rate(self, threshold:int):
        if self.progressbar_rate < self.progressbar_threshold:
            self.progressbar_rate = self.progressbar_threshold
        # 按zip进度百分比转1/3显示
        if self.src_zip_tmp_files:
            self.progressbar_threshold += int(threshold * 0.33)
        else:
            self.progressbar_threshold += threshold
        if self.progressbar_threshold > 999:
            self.progressbar_threshold = 999
        self.rate_timer.start(50, self)
        self.progressBar.setValue(self.progressbar_rate)


    # 设置zip进度条文字
    def set_zip_text(self, filename:str):
        self.label.setText("正在压缩 " + filename)
        SETTING.logger.info("压缩 " + filename)

    # 设置zip进度条
    def set_zip_progress(self, threshold:int):
        # 按zip进度百分比转2/3显示
        if self.progressbar_rate < int(self.progressbar_threshold * 0.66):
            self.progressbar_rate = int(self.progressbar_threshold * 0.66)
        self.progressbar_threshold += int(threshold * 0.66)
        if self.progressbar_threshold > 666:
            self.progressbar_threshold = 666
        self.rate_timer.start(50, self)
        self.progressBar.setValue(self.progressbar_rate)


    def timerEvent(self, event):
        if self.progressbar_rate >= self.progressbar_threshold:
            self.rate_timer.stop()
        else:
            self.progressbar_rate += 1
            self.progressBar.setValue(self.progressbar_rate)

    # cancel按钮点击事件
    def cancel_clicked(self):
        SETTING.logger.info("点击取消")
        # 设定全局变量标识，跨线程通信用Global类把变量传过去
        GlobalDict.set("cancel","canceled")
        self.rate_timer.stop()
        del self.rate_timer
        # 关闭自身
        self.close()
        self.exit_show_message("备份取消")

    # 弹窗
    def show_message(self,msg:str):
        QMessageBox.critical(self, "警告", msg,
                              QMessageBox.Ok)

    # 错误弹窗+退出,用于接收信号槽的中断备份操作
    def exit_show_message(self,msg:str):
        # 弹窗
        msg_box = QMessageBox.critical(self, "错误", msg,
                                       QMessageBox.Ok)
        # 删除zip列表中的源文件夹临时zip
        time.sleep(0.3)
        for i in self.zip_file_list:
            file = i +self.zip_tmpfile_suffix
            if is_root(file):
                file = add_tmp_path(file)
            try:
                SETTING.logger.info(f"删除临时压缩文件 {file}")
                os.remove(file)
            except OSError as e:
                SETTING.logger.error(e)

        if os.path.isdir(root_tmp_dir):
            SETTING.logger.info(f"删除临时文件夹 {root_tmp_dir}")
            try:
                shutil.rmtree(root_tmp_dir)
            except OSError as e:
                SETTING.logger.error(e)

        # 删除失败的备份
        if SETTING.Timestamp:
            backup_dir = SETTING.Target + '/Backup@' + SETTING.Timestamp
            if os.path.isdir(backup_dir):
                SETTING.logger.info(f"删除未完成的备份文件夹{backup_dir}")
                del_backup_dir(backup_dir)

        # 点OK，退出程序
        if msg_box == QMessageBox.Ok:
            SETTING.logger.info("备份中止")
            for w in QApplication.instance().allWidgets():
                if w != self:
                    del w
            ExitProgram.exit(1)

    def copy_error(self, err_msg):
        SETTING.logger.error(err_msg)
        self.exit_show_message(err_msg)

    # 复制完成后的清理，以及显示finish窗口
    def copy_finish(self, copid_file_list:list):
        SETTING.logger.info("所有文件复制完成")
        self.rate_timer.stop()
        self.close()
        # 删除zip列表中的源文件夹临时zip
        for i in self.src_zip_tmp_files:
            try:
                SETTING.logger.info(f"删除临时文件 {i}")
                os.remove(i)
            except OSError as e:
                SETTING.logger.error(e)
        if os.path.isdir(root_tmp_dir):
            try:
                SETTING.logger.info(f"删除临时目录 {root_tmp_dir}")
                shutil.rmtree(root_tmp_dir)
            except OSError as e:
                SETTING.logger.error(e)

        # 找到复制完成列表中后缀结束的项，改名
        if copid_file_list:
            for i in copid_file_list:
                if i.endswith(self.zip_tmpfile_suffix):
                    try:
                        SETTING.logger.info(f"重命名 {i}")
                        os.rename(i, i.replace(self.zip_tmpfile_suffix, ".zip"))
                    except OSError as e:
                        SETTING.logger.error(e)
            finish_window.show_finish()
        else:
            self.exit_show_message("没有备份任何文件")


# 后台压缩
class ZipFiles(Qt.QThread):

    # zip 文件列表
    zip_file_list:list = []
    # 已打包好zip的文件列表
    ziped_list:list = []
    # 后缀
    zip_tmpfile_suffix:str = ""
    # 定义信号槽
    zipping_signal = QtCore.pyqtSignal(str)
    ziprate_signal = QtCore.pyqtSignal(int)
    zipfinish_signal = QtCore.pyqtSignal(list)

    # 要打包的文件总大小MB
    total_sizeMB = 0.1
    # 已打包的文件大小
    ziped_sizeMB = 0.0
    # 操作被取消标识
    cancel = False

    # QThread入口
    def run(self):
        # 计算总文件大小
        for i in range(len(self.zip_file_list)):
            if os.path.isdir(self.zip_file_list[i]):
                for paths, _, filenames in os.walk(self.zip_file_list[i]):
                    for f in filenames:
                        self.total_sizeMB += os.stat(paths + "/" + f).st_size / 1024 / 1024
            else:
                self.total_sizeMB += os.stat(self.zip_file_list[i]).st_size / 1024 / 1024
        self.zip_file()



    # 整理列表，文件/文件夹分开操作
    def zip_file(self):
        for item in self.zip_file_list:
            if self.canceled():
                break
            # 如果是c盘根目录，建立临时目录
            if is_root(item):
                try:
                    if not os.path.isdir(root_tmp_dir):
                        os.mkdir(root_tmp_dir)
                except OSError as e:
                    self.cancel = True
                    SETTING.logger.error(e)
                    break
            # 判断是文件夹还是文件
            if os.path.isdir(item):
                zipname = self.zip_compress_dir(item, self.zip_tmpfile_suffix)
                self.ziped_list.append(zipname)
            else:
                zipname = self.zip_compress_file(item, self.zip_tmpfile_suffix)
                self.ziped_list.append(zipname)

        # 如果没有收到取消信号，发送已压缩的文件表到UI
        if not self.cancel:
            self.zipfinish_signal.emit(self.ziped_list)

    # 发送进度条阈值信号
    def send_rate(self):
        # 进度条当次阈值，按size计算百分比，最小1，最大99
        threshold = int(self.ziped_sizeMB / self.total_sizeMB * 1000)
        if threshold > 999:
            threshold = 999
        elif threshold < 1:
            threshold = 1
        self.ziprate_signal.emit(threshold)

    # 发送当前文件名信号
    def send_filename(self, filename):
        self.zipping_signal.emit(filename)

    # 取消
    def canceled(self) -> bool:
        # 如果被取消
        if GlobalDict.get("cancel") == "canceled":
            # 重置cancel标识变量
            GlobalDict.set("cancel", "")
            self.cancel = True
            return True
        else:
            return False

    # 压缩一个文件夹
    def zip_compress_dir(self, dirpath:str, suffix:str) -> str:
        zip_name = dirpath + suffix
        # 如果是c盘根目录，就把文件写入c盘下临时目录
        if is_root(zip_name):
            zip_name = add_tmp_path(zip_name)
        zip = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

        # 压缩文件夹下的所有文件
        for root, dirs, files in os.walk(dirpath):
            if self.canceled():
                break
            for file in files:
                if self.canceled():
                    break
                if str(file).startswith("~$"):
                    continue
                filename = os.path.join(root, file)
                self.send_filename(file)
                self.ziped_sizeMB += os.stat(filename).st_size / 1024 / 1024
                self.send_rate()
                in_zip_name = os.path.relpath(filename, os.path.dirname(dirpath))
                zip.write(filename, in_zip_name)
                self.send_rate()
        zip.close()
        return zip_name

    # 压缩一个文件
    def zip_compress_file(self, filename:str, suffix:str) -> str:
        self.ziped_sizeMB += os.stat(filename).st_size / 1024 / 1024
        _, pure_name = os.path.split(filename)
        zip_name = filename + suffix
        # 如果是c盘根目录，就把文件写入c盘下临时目录
        if is_root(zip_name):
            zip_name = add_tmp_path(zip_name)
        self.send_filename(pure_name)
        self.send_rate()
        zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
        zip.write(filename, pure_name)
        self.send_rate()
        zip.close()
        return zip_name


# 后台文件复制
class BackingUpFiles(Qt.QThread):


    # 待复制文件列表
    to_copy_list:list = []
    # 复制成功文件列表
    copid_file_list:list = []
    # 定义信号槽
    filename_signal = QtCore.pyqtSignal(str)
    rate_signal = QtCore.pyqtSignal(int)
    finish_signal = QtCore.pyqtSignal(list)
    copy_err_signal = QtCore.pyqtSignal(str)
    # 所有文件总大小
    total_sizeMB:float = 0.1
    # 已经拷贝的文件累计大小
    copid_files_sizeMB:float = 0.0
    # 当前进度条阈值
    threshold:int = 0
    # 文件计数变量
    copy_count:int = 0
    # 异常标识变量
    error_code:int = 0
    # 进度条变量
    rate:float = 0.0
    # 拷贝循环等待时间间隔
    timestep:float = 0.002
    # 进度条rate中止循环标识
    rate_loop_break:bool = False

    # QThread入口
    def run(self):
        # 设置本次备份的子文件夹名
        self.backup_dest_path = SETTING.Target + "/Backup@" + SETTING.Timestamp
        # 获取文件列表中所有文件的总大小
        self.total_sizeMB = self.get_total_size()
        # 判断剩余空间是否足够
        if sys.platform == "win32":
            dst_drive, _ = os.path.splitdrive(SETTING.Target)
        else:
            dst_drive = SETTING.Target
        i_ret = insufficient_space(dst_drive, self.total_sizeMB)
        # 如果错误，复制中断，返回错误码
        if i_ret == 0:
            # 开始备份
            self.backup_files()
        elif i_ret == -1:
            err_msg = f"目标磁盘{dst_drive}空间不足"
            self.copy_err_signal.emit(err_msg)
        elif i_ret == -2:
            err_msg = f"目标磁盘{dst_drive}找不到"
            self.copy_err_signal.emit(err_msg)


    def get_total_size(self) -> float:
        ret = 0.0
        for i in self.to_copy_list:
            filesizeMB = os.stat(i).st_size / 1024 / 1024
            ret += filesizeMB
        return ret


    # 复制列表中的文件
    def backup_files(self):
        # 复制文件子线程
        self.th_copy = File()
        # 复制完成的信号槽
        self.th_copy.copied_signal.connect(self.receive_copied)
        # 复制错误的信号槽
        self.th_copy.copy_err_signal.connect(self.copy_err_message)
        i = 0
        # 逐个复制列表中的文件
        for src_filename in self.to_copy_list:
            # 如果被中断则退出循环
            if i < 0:
                break
            # 整理目标文件名，去掉非法字符
            dst_filename = src_filename.replace(root_tmp_dir,"C:/")
            target_filename = (self.backup_dest_path + "/" +
                               cut_pathname_prefix(dst_filename.replace(":/","盘/")))
            # 打包子线程参数
            args = (self, src_filename, target_filename, SETTING.Target)
            # 给复制文件子线程传参数
            self.th_copy.args = args
            # 复制文件
            self.th_copy.start()
            # 通过信号槽发送文件名到UI
            _, filename = os.path.split(src_filename)
            self.filename_signal.emit(filename)
            # 获取当前文件大小，单位MB
            filesize = os.stat(src_filename).st_size / 1024 / 1024 +.000001
            self.copid_files_sizeMB += filesize
            # 进度条当次阈值，按size计算千分比，最小1，最大999
            self.threshold = int(filesize / self.total_sizeMB * 1000)
            if self.threshold > 999:
                self.threshold = 999
            elif self.threshold < 1:
                self.threshold = 1
            # 发送threshold到UI进度条显示
            self.rate_signal.emit(int(self.threshold))

            # 监视复制状态，等文件复制完成后继续
            i += 1
            while i > self.copy_count:
                time.sleep(self.timestep)
                # 如果被取消
                if GlobalDict.get("cancel") == "canceled":
                    # 重置cancel标识变量
                    GlobalDict.set("cancel", "")
                    # 设置错误信息
                    self.error_code = -2
                    self.rate_loop_break = True
                    # 中止外层循环
                    i = -1
                    # 延时0.2秒
                    time.sleep(0.3)
                    break
            # 当文件复制成功，设置进度条到匹配的位置
            self.copid_file_list.append(target_filename)
            self.rate = self.threshold

        # 如果没有发生错误，则弹窗finish
        if not self.error_code:
            self.finish()

    # 接收文件拷贝完成的信号槽函数
    def receive_copied(self, copied:bool):
        if copied:
            SETTING.logger.info("复制完成")
            self.copy_count += 1

    # 接收文件拷贝异常的信号槽函数
    def copy_err_message(self, msg:str):
        SETTING.logger.error("复制文件错误")
        self.rate_loop_break = True
        self.error_code = -1
        self.copy_err_signal.emit(msg)

    # 复制结束，发送信号到UI
    def finish(self):
        self.finish_signal.emit(self.copid_file_list)


# 完成窗口的GUI部件与业务逻辑
class FinishWidget(ui_finish.Ui_Form, QWidget):

    # 重写关闭事件，清除本程序的所有窗口实例，退出到系统
    def closeEvent(self, event):
        for w in QApplication.instance().allWidgets():
            if w != self:
                del w
        event.accept()
        ExitProgram.exit(0)

    # 设置按钮
    def setup_action(self):
        # 设置窗口无标题栏，透明，置顶
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint, True)
        # Mac版UI调整
        if not sys.platform == "win32":
            font = QFont()
            font.setFamily("Microsoft YaHei")
            font.setPointSize(12)
            self.lab_prompt.setFont(font)
        # 设置按钮
        self.btn_ok.clicked.connect(lambda : self.ok_clicked())
        self.btn_close.clicked.connect(lambda : self.ok_clicked())
        # 设置文字
        self.lab_prompt.setText("已成功备份到\n"
                                f"{SETTING.Target + '/Backup@' + SETTING.Timestamp}")

    # 拖动窗口鼠标按下事件
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            super(FinishWidget, self).mousePressEvent(event)
            self.start_x = event.x()
            self.start_y = event.y()

    # 拖动窗口鼠标弹起事件
    def mouseReleaseEvent(self, event):
        self.start_x = None
        self.start_y = None

    # 拖动窗口鼠标按住拖动事件
    def mouseMoveEvent(self, event):
        super(FinishWidget, self).mouseMoveEvent(event)
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x() + dis_x, self.y() + dis_y)


    # ok按钮点击事件
    def ok_clicked(self):
        SETTING.logger.info("完成")
        self.close()
        # 退出
        ExitProgram.exit(0)


# 完成窗口
class FinishWindow:

    def show_finish(self):
        try:
            file_window.edit_list.hide()
            backing_window.backing_up.hide()
        except:
            pass
        self.finish = FinishWidget()
        self.finish.setupUi(self.finish)
        self.finish.setup_action()
        self.finish.show()


# 进度条
class BackingWindow:

    def show_backing(self):
        try:
            file_window.edit_list.hide()
            finish_window.finish.hide()
        except:
            pass
        self.backing_up = BackingWidget()
        self.backing_up.setupUi(self.backing_up)
        self.backing_up.setup_action()
        self.backing_up.show()


# 文件管理窗口
class FileWindow:

    def show_edit_list(self):
        self.edit_list = EditListWidget()
        self.edit_list.setupUi(self.edit_list)
        self.edit_list.setup_action()
        self.edit_list.show()


    def goto_files_widget(self):
        try:
            backing_window.backing_up.hide()
            finish_window.finish.hide()
        except:
            pass
        self.show_edit_list()


# 退出
class ExitProgram:

    def exit(self, errcode=0):
        backup_dest_path = SETTING.Target + "/Backup@" + SETTING.Timestamp
        if os.path.isdir(backup_dest_path):
            # 复制log文件到备份文件夹
            log_file = res_path("backup.log")
            backup_dest_path = SETTING.Target + "/Backup@" + SETTING.Timestamp
            try:
                shutil.copy(log_file, backup_dest_path +"/"+ SETTING.Timestamp + ".备份日志.log")
            except OSError as e:
                SETTING.logger.error(e)
        # 退出
        os._exit(errcode)


# 程序入口
if __name__ == "__main__":
    # 全局变量
    SETTING = Setting()
    # 设置在windows超分辨率下窗口的正常显示
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    # 设置GUI主程序
    app = QApplication(sys.argv)
    # 定义窗口实例
    file_window = FileWindow()
    backing_window = BackingWindow()
    finish_window = FinishWindow()
    # 显示file_windows
    file_window.show_edit_list()
    # GUI主循环
    sys.exit(app.exec_())