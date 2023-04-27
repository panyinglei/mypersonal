import pandas as pd
from Config.globalUsedSetting import USED_FILE_ROOT as FIlle

# 读取excel
def readExcelAnalize(filePath):
    data = pd.read_excel(filePath, header=0 , sheet_name="Sheet1")
    datamsg = []
    for i in range(len(data['基本信息'])-1):
        datamsg.append([data['基本信息'][i+1],data['Unnamed: 1'][i+1],data['请求信息'][i+1],data['Unnamed: 3'][i+1],
                    data['Unnamed: 4'][i+1],data['Unnamed: 5'][i+1],data['Unnamed: 6'][i+1],data['响应信息'][i+1],
                    data['Unnamed: 8'][i+1],data['Unnamed: 9'][i+1],data['保存参数'][i+1],])
    return datamsg


# 分割字符串
def spliteMessage(msg):
    if ";" in msg:
        return str.split(msg, ';')
    else:
        return str.split(msg, ':')

# 转为字典


