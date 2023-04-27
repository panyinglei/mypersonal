import copy
import json

import ddt
import os
import Config.globalUsedSetting

from Tool.doQuest import doQuest
from Tool.ReadApiExcel import readExcelAnalize, spliteMessage
from Tool.base64Analize import scriptAnlize
import allure
import pytest

from Config.globalUsedSetting import USED_FILE_ROOT,GLOBAL_SCRIPT

class TestApiCla():

    dataMsg = readExcelAnalize( USED_FILE_ROOT["TestCaseXlsx"] )
    # dataMsg = pd.read_excel("../FIle/excel/4-接口文档解析模版.xlsx", header=0 , sheet_name="Sheet1")

    @allure.story(dataMsg[0][1])
    @pytest.mark.parametrize('data',dataMsg)
    def test_BTLcase(self,data):
        # 读取数据
        header = json.loads(data[4])
        requeData = json.loads(data[5])
        assertRespData = json.loads(data[8])
        saveGlobalParams = json.loads(data[10])



        # 判断是否有在全局中拿取的参数,暂时需要根据实际情况进行调整（调整GLOBAL_SCRIPT中相应的数据名称）
        for i in requeData:
            for j in requeData[i]:
                if requeData[i][j] is None:
                    requeData[i][j] = GLOBAL_SCRIPT[j]

        # 发起请求
        respData = doQuest.sendQuest(None, data[2], data[3], header, requeData)
        print(respData.json())

        # 判断是否有需要保存的参数
        # for i in saveGlobalParams:
        #     tier = str.split(i, ".")
        #     GLOBAL_SCRIPT[i] = getJsonData(respData.json(), tier)
        #     print(getJsonData(respData.json(), tier))



        # 验证码识别获取,暂时还需要根据相应情况进行更改
        if "picPath" in str(respData.json()):
            GLOBAL_SCRIPT["picPath"] = str.split(respData.json()["data"]["picPath"], ",")[1]
            GLOBAL_SCRIPT["captcha"] = scriptAnlize(GLOBAL_SCRIPT["picPath"])
            print(GLOBAL_SCRIPT["picPath"])
        # 获取登录后的token
        if "token" in str(respData.json()):
            GLOBAL_SCRIPT["token"] = respData.json()["data"]["picPath"]
        print(respData.json())
        # # 断言
        # for i in assertRespData:
        #     # print(i.decode("utf-8"))
        #     print(respData)
        #
        #     # print(respData.json()[i])
        #     print(assertRespData[i])
        #     assert respData.json()[i] == assertRespData[i]


def getJsonData(direct,key):
    if len(key) == 1 :
        return direct[key[0]]
    key2 = copy.copy(key)
    del key2[0]
    json = getJsonData(direct[key[0]],key2)
    return json