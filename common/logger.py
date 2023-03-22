import logging
import os

logger = logging.getLogger("dyd-测试日志")    # 定义日志并设置名称然后赋值给logger
logger.setLevel(logging.DEBUG)				# 设置日志为DEBUG级别

# 定义日志格式，输出格式为：当前时间 - 日志等级 - 函数名 - 日志信息
format = logging.Formatter("%(asctime)s - %(levelname)s - %(funcName)s - %(message)s")
yd = logging.StreamHandler()  # 输出日志记录
yd.setFormatter(format)  # 输出日志使用定义的format格式
logger.addHandler(yd)   # 日志输出到控制台

# 定义日志存放目录
log = os.path.join(os.path.dirname(__file__), "../logs")    # 获取当前路径，返回上一级进入logs目录
if not os.path.exists(log):  # 如果logs目录不存在，就先创建logs目录
    os.mkdir(log)
logfiles = os.path.join(log, "APItest.log")
re = logging.FileHandler(logfiles)  # 日志记录到指定文件中
re.setFormatter(format)  # 输出日志使用定义的format格式
logger.addHandler(re)   # 日志输出到控制台
