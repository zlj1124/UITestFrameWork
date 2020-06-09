'''
@Descripttion: 
@Author: zlj
@Date: 2019-12-05 11:05:13
'''
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile


class HomePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # title
    title = do_conf.get_locators_or_account('HomePageElements', 'title')
    # 首页
    homePage = do_conf.get_locators_or_account('HomePageElements', 'homePage')
    # 监控
    monitor = do_conf.get_locators_or_account('HomePageElements', 'monitor')
    # 报警
    alarm = do_conf.get_locators_or_account('HomePageElements', 'alarm')
    # 车辆
    vehicle = do_conf.get_locators_or_account('HomePageElements', 'vehicle')
    # 统计
    statistics= do_conf.get_locators_or_account('HomePageElements', 'statistics')
    # 设置
    settings = do_conf.get_locators_or_account('HomePageElements', 'settings')
   

    def select_menu(self, menu='settings'):
         
        self.click_title_menu()
        if menu == "monitor":
            self.click_monitor_menu()
        elif menu == 'homePage':
            self.click_home_page_menu()
        elif menu == 'alarm':
            self.click_alarm_menu()
        elif menu == 'truck':
            self.click_vehicle_menu()
        elif menu == 'statistics':
            self.click_statistics_menu()
        elif menu == 'settings':
            self.click_settings_menu()


        else:
            raise ValueError(
                '''菜单选择错误!
                homePage->首页
                monitor->监控
                alarm->报警
                truck->车辆
                statistics->统计
                setting->设置'''
            )
    def click_title_menu(self):
        return self.move_to_element(*HomePage.title)

    def click_home_page_menu(self):
        return self.click(*HomePage.homePage)

    def click_monitor_menu(self):
        return self.click(*HomePage.monitor)

    def click_alarm_menu(self):
        return self.click(*HomePage.alarm)

    def click_vehicle_menu(self):
        return self.click(*HomePage.vehicle)

    def click_statistics_menu(self):
        return self.click(*HomePage.statistics)  

    def click_settings_menu(self):
        return self.click(*HomePage.settings)    


if __name__ == '__main__':
    pass
