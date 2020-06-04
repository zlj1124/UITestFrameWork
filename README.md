# UITestFrameWork
    Pytest_UI框架
    说明：

    环境需求：
        2.需安装python 3.以上版本
        3.selenium 2 以上版本
        4.需安装pytest框架
        5.需安装pytest -html插件
        6.需安装谷歌浏览器及对应驱动
        7.需对发送测试报告邮件的邮箱正确配置
        9.需要安装openpyxl数据处理库
        10.需要安装yagmail库发送测试报告
    运行项目：
        1.下载项目到本地
        2.打开cmd切换到项目根目录
        3.输入python RunTestCase.py运行项目
        4.或者直接通过pytest --html=’report.html‘ 运行(这种方式不会自动发送测试邮件)
        5.生成allure报告
            1. py.test TestCases/test_loginCase.py  --alluredir ./result/
            2.allure generate ./result/ -o ./report/ --clean 
            
      

    
    