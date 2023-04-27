import allure
import json
import jsonpath
import requests
from urllib3 import encode_multipart_formdata


# 请求类
class doQuest():

    @allure.step("发送请求")
    def sendQuest(self, url, method, headers, requestdata):
        # 判断requestdata中是否包含某些数据
        # try:
        if ("params" in requestdata):
            return requests.request(url=url, method=method, headers=headers, params=requestdata["params"])
        elif ("data" in requestdata ):
            return requests.request(url=url, method=method, headers=headers, data=requestdata["data"])
        elif ("json" in requestdata):
            return requests.request(url=url, method=method, headers=headers, json=requestdata["json"])
        else:
            return requests.request(url=url, method=method, headers=headers)
        # if ("params" in requestdata) and ("data" not in requestdata) :
        #     return requests.request(url=url, method=method, headers=headers, params=requestdata["params"])
        # elif ("params" not in requestdata) and ("data" in requestdata):
        #     return requests.request(url=url, method=method, headers=headers, data=requestdata["data"])
        # else :
        #     return requests.request(url=url, method=method, headers=headers)

        # except Exception as e:
        #     # print(type(e))
        #     return e



    @allure.step("请求参数中包含文件")
    def post_files(self, url, filepath, method, headers, data=None):
        # headers为字典
        # # 第一种方法：
        # with open(filepath, 'rb') as f:
        #     file = {"file": ("filename", f.read())
        #             # key：value（上传图片时有时附带其他字段时，选填）
        #             }
        #     encode_data = encode_multipart_formdata(file)
        #     file_data = encode_data[0]
        #     header = {'Content-Type': encode_data[1]}  # 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4'
        #     res = requests.post(url, headers=header, data=file_data).json()
        #
        # print(res)
        # 第二种方法：

        file_data = {'file':  open(filepath, 'rb').read()
                     # key：value（上传图片时有时附带其他字段时，选填）
                     }
        encode_data = encode_multipart_formdata(file_data)
        data = encode_data[0]  # b'--c0c46a5929c2ce4c935c9cff85bf11d4\r\nContent-Disposition: form-data; name="file"; filename="1.txt"\r\nContent-Type: text/plain\r\n\r\n...........--c0c46a5929c2ce4c935c9cff85bf11d4--\r\n
        header = {'Content-Type': encode_data[1]}  # 'Content-Type': 'multipart/form-data; boundary=c0c46a5929c2ce4c935c9cff85bf11d4'
        header.update(headers)
        return requests.request(url=url,  method=method, headers=header, data=data)

    # 由于接口之间可能相互关联，因此下一个接口需要上一个接口的某个返回值，此处采用jsonpath对上一个接口返回的值进行定位并取值
    # @allure.step("获取返回结果字典值")
    # def get_text(self, data, key):
    #     # json数据转换为字典
    #     json_data = json.loads(data)
    #     # jsonpath取值
    #     value = jsonpath.jsonpath(json_data, '$..{0}'.format(key))
    #     return value[0]



