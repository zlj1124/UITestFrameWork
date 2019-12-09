
import sys
import pytest

from config.conf import ROOT_DIR, HTML_NAME,SMTP_SERVER,FROM_USER,FROM_PASSWORD,TO_USER,SUBJECT,CONTENTS,HTML_NAME

from util.sendMailForReprot import SendMailWithReport


def main():
    if ROOT_DIR not in sys.path:
        sys.path.append(ROOT_DIR)
    # 执行用例
    args = ['--reruns', '0', '--html=' + './report/' + HTML_NAME]
    pytest.main(args)
   
    # 发送邮件 
    HTML=ROOT_DIR+'/report/testReport.html'
    SendMailWithReport.send_mail(
        SMTP_SERVER, FROM_USER, FROM_PASSWORD,
        TO_USER, SUBJECT, CONTENTS,HTML)


if __name__ == '__main__':
    main()

