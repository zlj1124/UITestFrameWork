<!--
 * @Descripttion: 
 * @Author: zlj
 * @Date: 2019-12-09 16:43:55
-->
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

## 目录结构
```
.
├── assets  
│   └── style.css
├── config
│   ├── __init__.py
│   ├── conf.py   ———— 邮件配置，目录常量
│   ├── config.ini ———— 元素定位
│   └── db.ini  ———— 数据库配置（host,port,user,password,db_name,charset）
├── data  ———— 数据源
│   ├── __init__.py
│   ├── attachment
│   ├── login_data.py
│   ├── tcData.xlsx
│   ├── truckmodel.xlsx
│   └── worker_data.py
├── drivers
│   └── chromedriver
├── Page
│   ├── __init__.py
│   ├── BasePage.py   ———— 封装一些selenium内置方法
│   ├── PageObject  ————业务逻辑函数
│       ├── __init__.py
│       ├── HomePage.py
│       ├── LoginPage.py
│       ├── ProfilePage.py
│       ├── TruckPage.py
│ 
├── TestCases ————测试用例
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_ProfileCase.py
│   ├── test_loginCase.py
│   └── test_uploadfile.py
│ 
├── report ————allure测试报告
│   ├── app.js
│   ├── assets
│   ├── data
│   ├── export
│   ├── history
│   ├── index.html
│   ├── plugins
│   ├── styles.css
│   ├── testReport.html
│   └── widgets
│── util
│    ├── __init__.py
│    ├── db.py ———— 封装sql函数
│    ├── parseConFile.py   ———— 相关解析函数
│    ├── parseDB.py
│    ├── parseExcelFile.py
│    └── sendMailForReprot.py ———— 发送报告邮件函数
│
├── conftest.py
├── pytest.ini
├── RunTestCase.py   ———— 入口函数
├── requirements.txt
└── README.md


```    
    