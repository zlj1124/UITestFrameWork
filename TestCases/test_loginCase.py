
import pytest
import time
from data.login_data import LoginData
from util.parseExcelFile import ParseExcel
import allure

@allure.feature('login功能')
# @pytest.mark.loginTest
class TestLogin(object):
    """登录"""
    login_data = LoginData
    data=ParseExcel()
    sheet=data.get_sheet_by_name('login')
    
    #数据源使用类
    @pytest.mark.skip()  
    @allure.story('login_sucess')
    @pytest.mark.parametrize('username, password, expect', login_data.login_success_data)
    def test_login(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password) 
        actual = login_page.get_login_success_account()
        assert expect in actual, "登录成功"
  

    #数据源使用Excel   
    @allure.story('login_faild')
    # @pytest.mark.skip()  
    @pytest.mark.parametrize('username, password, expect',data.get_all_values_of_sheet(sheet))
    def test_fail(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_error_text()
        print("expect:{},actual:{}".format(expect,actual))
        assert actual == expect, "登录失败, 断言失败"


     

if __name__ == "__main__":
    pytest.main(['-s', 'test_loginCase.py'])
