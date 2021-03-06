
import time
from selenium.webdriver.support.wait import WebDriverWait as WD
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import (
    TimeoutException,
    NoAlertPresentException,
)

# from util.clipboard import ClipBoard
# from util.keyboard import KeyBoard
from util.parseConFile import ParseConFile
from util.parseExcelFile import ParseExcel


class BasePage(object):
    """结合显示等待封装一些selenium内置方法"""
    cf = ParseConFile()
    excel = ParseExcel()

    def __init__(self, driver, timeout=30):
        self.byDic = {
            'id': By.ID,
            'name': By.NAME,
            'class_name': By.CLASS_NAME,
            'xpath': By.XPATH,
            'link_text': By.LINK_TEXT
        }
        self.driver = driver
        self.outTime = timeout

    def find_element(self, by, locator):
        """
        查找单个元素
        """
        try:
            print('[Info:Starting find the element "{}" by "{}"!]'.format(locator, by))
            element = WD(self.driver, self.outTime).until(lambda x: x.find_element(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return element

    def find_elements(self, by, locator):
        """
        查找一组元素
        """
        try:
            print('[Info:start find the elements "{}" by "{}"!]'.format(locator, by))
            elements = WD(self.driver, self.outTime).until(lambda x: x.find_elements(by, locator))
        except TimeoutException as t:
            print('error: found "{}" timeout!'.format(locator), t)
        else:
            return elements

    def is_element_exist(self, by, locator):
        """
       判断元素可见
        """
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(EC.visibility_of_element_located((self.byDic[by], locator)))
            except TimeoutException:
                print('Error: element "{}" not exist'.format(locator))
                return False
            return True
        else:
            print('the "{}" error!'.format(by))

    def is_click(self, by, locator):
        """元素可点击"""
        if by.lower() in self.byDic:
            try:
                element = WD(self.driver, self.outTime). \
                    until(EC.element_to_be_clickable((self.byDic[by], locator)))
            except TimeoutException:
                print("元素不可以点击")
            else:
                return element
        else:
            print('the "{}" error!'.format(by))

    def is_alert(self):
        """
        判断alert弹框存在
        """
        try:
            re = WD(self.driver, self.outTime).until(EC.alert_is_present())
        except (TimeoutException, NoAlertPresentException):
            print("error:no found alert")
        else:
            return re

    def switch_to_frame(self, by, locator):
        """判断frame是否存在，存在就跳到frame"""
        print('info:switching to iframe "{}"'.format(locator))
        if by.lower() in self.byDic:
            try:
                WD(self.driver, self.outTime). \
                    until(EC.frame_to_be_available_and_switch_to_it((self.byDic[by], locator)))
            except TimeoutException as t:
                print('error: found "{}" timeout！切换frame失败'.format(locator), t)
        else:
            print('the "{}" error!'.format(by))

    def switch_to_default_frame(self):
        """返回默认的frame"""
        print('info:switch back to default iframe')
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    def get_alert_text(self):
        """获取alert的提示信息"""
        alert = self.is_alert()
        if alert:
            return alert.text
        else:
            return None

    def get_element_text(self, by,locator=None):

        """获取某一个元素的text信息"""

        try:
         
            element = WD(self.driver, 30).until(
            EC.visibility_of_element_located((self.byDic[by], locator)))

            # element = WD(self.driver,30).until(
            #     EC.presence_of_element_located((self.byDic[by], locator))
            # )                                  
            print("element.text:{}".format(element.text))

            return element.text
        except AttributeError:
            print('get "{}" text failed return None'.format(locator))

    def load_url(self, url):
        """加载url"""
        print('info: string upload url "{}"'.format(url))
        self.driver.get(url)

    def get_source(self):
        """获取页面源码"""
        return self.driver.page_source

    def get_currenturl(self):
        """获取当前页的url"""
        return self.driver.current_url

    def send_keys(self, value, by,locator=''):
        """写数据"""
        print('info:input "{}"'.format(value))
        try:
            element= WD(self.driver, 30).until(
            EC.presence_of_element_located((by, locator)))
            element.send_keys(value)
            time.sleep(1)
        except AttributeError as e:
            print(e)

    def clear(self, by, locator):
        """清理数据"""
        print('info:clearing value')
        try:
            element = self.find_element(by, locator)
            element.clear()
        except AttributeError as e:
            print(e)

    def click(self, by, locator):
        """点击某个元素"""
        print('info:click "{}"'.format(locator))
        element = self.is_click(by, locator)
        if element!=None:
            element.click()
        else:
            print('the "{}" unclickable!')

    def move_to_element(self, by, locator):
        """移动至某个元素"""
        print('info:moveto "{}"'.format(locator))

        element=self.find_element(by,locator)
        if element:
            webdriver.ActionChains(self.driver).move_to_element(element).click().perform()   
            time.sleep(1) 
        else:
            print('the "{}" unclickable!')
        


    @staticmethod
    def sleep(num=0):
        """强制等待"""
        print('info:sleep "{}" minutes'.format(num))
        time.sleep(num)

    # def ctrl_v(self, value):
    #     """ctrl + V 粘贴"""
    #     print('info:pasting "{}"'.format(value))
    #     ClipBoard.set_text(value)
    #     self.sleep(3)
    #     KeyBoard.two_keys('ctrl', 'v')

    # @staticmethod
    # def enter_key():
    #     """enter 回车键"""
    #     print('info:keydown enter')
    #     KeyBoard.one_key('enter')

    def wait_element_to_be_located(self, by, locator):
        """显示等待某个元素出现"""
        print('info:waiting "{}" to be located'.format(locator))
        try:
            return WD(self.driver, self.outTime).until(EC.presence_of_element_located((self.byDic[by], locator)))
        except TimeoutException as t:
            print('error: found "{}" timeout！'.format(locator), t)

    def get_page_source(self):
        return self.get_source()


if __name__ == "__main__":
    pass
