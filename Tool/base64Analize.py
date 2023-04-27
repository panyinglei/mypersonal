# 分析
import time

import  cv2
import base64
import numpy as np
import ddddocr
import time
# from aip import AipOcr
# import pytesser3
# import pytesseract
# from PIL import Image
from Config.globalUsedSetting import USED_FILE_ROOT

def base64TurnPic(base64_img):
    # 解码图片
    imgdata = base64.b64decode(base64_img)
    # 将图片保存为文件
    with open(USED_FILE_ROOT["Picture"], 'wb') as f:
        f.write(imgdata)

# 普通验证码操作流程
def pictureAnalize():
    # 灰度化
    yzm = cv2.imread('../FIle/picture/1.jpg')
    yzm = cv2.cvtColor(yzm, cv2.COLOR_BGR2GRAY)
    # 二值化
    thresh, yzm = cv2.threshold(yzm, 30, 40, cv2.THRESH_BINARY)
    # yzm:表示需要操作的数组
    # 160:表示阈值
    # 255 表示最大值
    # 降噪
    yzm = cv2.morphologyEx(yzm, cv2.MORPH_CLOSE, np.ones(shape=(6, 6)))
    # 先膨胀 让黑色遭点消失，再侵蚀让黑色加粗（降噪）
    dilate = cv2.dilate(yzm, np.ones(shape=(6, 6)))
    yzm = cv2.erode(dilate, np.ones(shape=(5, 5)))
    # # muggle_ocr识别
    # sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
    # img = open('2.png', 'rb').read()
    # text = sdk.predict(image_bytes=img)
    # print(text)
    # pytesser3识别
    cv2.imwrite('../FIle/picture/2.png', yzm)  # 写入
    # text = pytesser3.image_file_to_string('../FIle/picture/2.png')
    # return text

# 使用ddddorc识别验证码
def scriptAnlize(base64_img):
    base64TurnPic(base64_img)
    begin = time.time()
    ocr = ddddocr.DdddOcr()

    with open(USED_FILE_ROOT["Picture"], 'rb') as f:
        img_bytes = f.read()

    res = ocr.classification(img_bytes)
    finish = time.time()
    return res
    # print("结果：")
    # print(res)
    # print("用时：%s 秒" % str(finish - begin))


    # # open的是图片的路径
    #
    # image = Image.open('../FIle/picture/1.jpg')
    #
    # code = pytesseract.image_to_string(image)
    # # time.sleep(10)
    #
    # print(code)
    # print(type(code))

#
# base64TurnPic("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"
#               "")
#
# scriptAnlize()