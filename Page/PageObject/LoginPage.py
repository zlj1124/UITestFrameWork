import time
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class LoginPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 登录失败的提示信息
    error_head = do_conf.get_locators_or_account('LoginPageElements', 'errorHead')
    # 登录成功后的用户显示元素
    account = do_conf.get_locators_or_account('HomePageElements', 'account')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
        time.sleep(1)
        

    def open_url(self):
        return self.load_url('http://47.110.188.32:80/login')

   

    def clear_username(self):
        return self.clear(*LoginPage.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(username,*LoginPage.username)

    def clear_password(self):
        return self.clear(*LoginPage.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(password,*LoginPage.password)

    def click_login_btn(self):
        return self.click(*LoginPage.loginBtn)

    def switch_default_frame(self):
        return self.switch_to_default_frame()

    def get_error_text(self):
       
        return self.get_element_text(*LoginPage.error_head)

    def get_login_success_account(self): 
        return self.get_element_text(*LoginPage.account)


if __name__ == "__main__":
    pass
