'''
本模块:自动获取项目下各个包的路径
'''
import os
#获取当前项目的路径
path=os.path.dirname(os.path.dirname(__file__))

#Config包的路径
config_Path=os.path.join(path,"Config","")
#Data包的路径
data_Path=os.path.join(path,"ReportFile","")
#Report目录的路径
report_Path=os.path.join(path,"Report","")
#Testcase包的路径
testcase_Path=os.path.join(path,"Testcase","")
#Unitils包的路径
untils_Path=os.path.join(path,"Untils","")
#email.ini文件的路径
email_Path=os.path.join(data_Path,"email.ini")
#contrl.ini
contrl_Path=os.path.join(data_Path,"contrl.ini")
#environment.ini
env_Path=os.path.join(data_Path,"environment.ini")

bady_Path=os.path.join(data_Path,'bady.xls')

# print(yaml_Path)
