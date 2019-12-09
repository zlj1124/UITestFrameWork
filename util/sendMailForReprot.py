

import yagmail


class SendMailWithReport(object):
    """发送邮件"""

    @staticmethod
    def send_mail(smtp_server, from_user, from_pass_word, to_user, subject, content, file_name):
        # 初始化服务器等信息
        yag = yagmail.SMTP(from_user, from_pass_word, smtp_server)
        # 发送邮件
        yag.send(to =to_user, subject = subject, contents=[file_name,'/Users/test/work/UITest/util/1.png'])




if __name__ == '__main__':
    SendMailWithReport.send_mail('smtp.mxhichina.com',
                                 'zuolj@burnish.cn',
                                 'My334420',
                                 'zuolj@burnish.cn',
                                 'python自动化测试',
                                 '邮件正文',
                                 './report/testReport15_38_54.html')
