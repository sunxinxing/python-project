

'''
日志模块级别:
debug
info
warning
error
critical
'''

import logging
from os import name
'''
logging.basicConfig(level="ERROR")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

'''



#定义日志器（实例化日志对象）
log = logging.getLogger()
log.setLevel("ERROR")
# name = log.name



#定义日志打印格式。
fmt = "%(name)s-->%(levelname)s--->%(asctime)s--->%(message)s"


#创建格式器
get_fmt = logging.Formatter(fmt=fmt)

#定义处理器（将日志输出到控制台）
console = logging.StreamHandler()
console.setLevel("INFO")
console.setFormatter(get_fmt)


#将日志器添加处理器
log.addHandler(console)



'''
#定义日志器（实例化日志对象）
log = logging.getLogger()
log.setLevel("WARNING")

#定义日志打印格式。
fmt = "%(name)s-->%(levelname)s--->%(asctime)s--->%(message)s"


#创建格式器
get_fmt = logging.Formatter(fmt=fmt)



#定义处理器（将日志输出到文件）
console = logging.FileHandler("./log.txt", mode="a", encoding="utf8")
console.setLevel("INFO")
console.setFormatter(get_fmt)



#将日志器添加处理器
log.addHandler(console)

'''
logging.basicConfig(level="ERROR")
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")