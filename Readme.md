# 持续更新中，个人使用，项目并不完善
# 使用时按照excel文档中的格式进行apipost的测试用例编写，直接运行apipost即可
# 其中使用的参数部分需要手动更改代码

运行生成allure测试报告

pytest [测试文件] -s -q --alluredir=[报告文件输出地址]

直接打开查看

allure serve [报告文件输出地址]

生成报告

allure generate [报告文件输出地址] -o [html报告生成地址] --clean 

打开

allure open -h 127.0.0.1 -p 8883 [html报告生成地址]















