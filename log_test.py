# 日志部分
root = logging.getLogger('init.log')
## 设置登记
root.setLevel(logging.DEBUG)
## 设置日志文件
fh = logging.FileHandler("./log/__init__.log")
# 设置日志数据流的句柄
handler = logging.StreamHandler()
## 设置日志格式化方式
logfmt = logging.Formatter('{asctime} {name} {levelname:8s} {message}',style='{')
## 通过日志数据流的句柄 格式化 数据流
handler.setFormatter(logfmt)
root.addHandler(handler)
## 为日志流添加目的文件
logger = logging.getLogger('__init__.py')
logger.
