运行生成allure测试报告

pytest [测试文件] -s -q --alluredir=[报告文件输出地址]

直接打开查看

allure serve [报告文件输出地址]

生成报告

allure generate [报告文件输出地址] -o [html报告生成地址] --clean 

打开

allure open -h 127.0.0.1 -p 8883 [html报告生成地址]
















欢迎使用ddddocr，本项目专注带动行业内卷，个人博客:wenanzhe.com
训练数据支持来源于:http://146.56.204.113:19199/preview
爬虫框架feapder可快速一键接入，快速开启爬虫之旅：https://github.com/Boris-code/feapder
谷歌reCaptcha验证码 / hCaptcha验证码 / funCaptcha验证码商业级识别接口：https://yescaptcha.com/i/NSwk7i