
import pytest
import time
from data.login_data import LoginData


# @pytest.mark.loginTest
class TestLogin(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password, expect', login_data.login_success_data)
    def test_login(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        time.sleep(1)
        
        # actual = login_page.get_login_success_account()
        # print("expect:{},actual:{}".format(expect,actual))
        # assert expect in actual, "登录成功"

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_data)
    def test_fail(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_error_text()
        print("expect:{},actual:{}".format(expect,actual))
        assert actual == expect, "登录失败, 断言失败"


if __name__ == "__main__":
    pytest.main(['-s', 'test_loginCase.py'])
