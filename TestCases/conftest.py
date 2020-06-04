'''
@Descripttion: 
@Author: zlj
@Date: 2019-12-05 11:05:13
'''

import pytest
from Page.PageObject.LoginPage import LoginPage
from Page.PageObject.HomePage import HomePage
from Page.PageObject.ProfilePage import ProfilePage
from util.parseConFile import ParseConFile


do_conf = ParseConFile()
# 从配置文件中获取正确的用户名和密码
userName = do_conf.get_locators_or_account('LoginAccount', 'username')
passWord = do_conf.get_locators_or_account('LoginAccount', 'password')


# @pytest.fixture(scope='function')
# def login(driver):
#     """除登录用例，每一个用例的前置条件"""
#     print('------------staring login------------')
#     login_action = LoginPage(driver, 30)
#     login_action.login(userName, passWord)
#     yield
#     print('------------end login------------')
#     driver.delete_all_cookies()

@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)
    profile_page = ProfilePage(driver)
    # yield生成器实例化pageobject
    yield driver, login_page, home_page, profile_page


@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    yield login_page
    driver.delete_all_cookies()


@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page, home_page,profile_page = ini_pages
    login_page.login(userName, passWord)
    yield login_page, home_page, profile_page 
    driver.delete_all_cookies()


@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()
