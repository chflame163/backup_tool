# 可以跨模块跨线程使用的全局变量
# 在模块头部导入
# from globalDict import GlobalDict
# 在任何地方使用下列方式访问
# GlobalDict.get("keyname")获取变量，如果keyname不存在则返回False
# GlobalDict.set("keyname",value)设置变量

class GlobalDict:

    def set( key:str, value:str):
        global _dict
        # 如果字典不存在则用新建空字典替换之
        tmp = {}
        try:
            tmp = _dict
        except:
            pass
        _dict = tmp

        # 添加值到变量
        _dict[key] = value

    def get(key:str) -> str:
        try:
            return _dict[key]
        except:
            return ""
