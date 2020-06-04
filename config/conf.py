
from datetime import datetime
import os
#测试地址
URL=" http://192.168.3.21:18082"
# 项目根目录
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 报告目录
REPORT_DIR = os.path.join(ROOT_DIR, 'report')
# ui对象库config.ini文件所在目录
CONF_PATH = os.path.join(ROOT_DIR, 'config', 'config.ini')
DB_PATH = os.path.join(ROOT_DIR,'config','db.ini')
# 测试数据所在目录
DATA_Path = os.path.join(ROOT_DIR, 'data', 'tcData.xlsx')
DATA_JsonPath = os.path.join(ROOT_DIR, 'data', 'data.json')

# 当前时间
CURRENT_TIME = datetime.now().strftime('%H_%M_%S')

# 邮件配置信息
# 邮件服务器
SMTP_SERVER = 'smtp.qq.com'
# 发送者
FROM_USER = '2205663173@qq.com'
# 发送者密码
FROM_PASSWORD ='wbsgbxqylvipdjhi'
# 接收者
TO_USER = ['zuolj@burnish.cn']  # 可以同时发送给多人，追加到列表中
# 邮件标题
SUBJECT = '自动化测试报告'
# 邮件正文
CONTENTS = '测试报告正文'
# 报告名称
# HTML_NAME = 'testReport{}.html'.format(CURRENT_TIME)
HTML_NAME = 'testReport.html'
