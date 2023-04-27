import os
from datetime import time


# 运行测试用例
os.system("pytest [测试文件] -s -q --alluredir=./File/report" + time.strftime("%Y%m%d%H%M%S", time.localtime()))
