
from Page.BasePage import BasePage
from util.parseConFile import ParseConFile
import time

class ProfilePage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile()
    # 新键worker按钮
    new_worker_btn = do_conf.get_locators_or_account('ProfilePageElements', 'new_worker')
    # 修改worker按钮
    alter_worker_btn = do_conf.get_locators_or_account('ProfilePageElements','alter_worker')
    #删除worker按钮
    delete_worker_btn=do_conf.get_locators_or_account('ProfilePageElements','delete_worker')
    # 姓名输入框
    name = do_conf.get_locators_or_account('ProfilePageElements', 'name')
    # 电话输入框
    phone = do_conf.get_locators_or_account('ProfilePageElements', 'phone')
    # 部门输入框
    department = do_conf.get_locators_or_account('ProfilePageElements', 'department')
    # 确定按钮
    commit  = do_conf.get_locators_or_account('ProfilePageElements', 'commit')
    # 删除确定按钮
    commit_del  = do_conf.get_locators_or_account('ProfilePageElements', 'delete_btn')
    #信息行
    item = do_conf.get_locators_or_account('ProfilePageElements','item')
    # 添加的提示信息
    add_tip = do_conf.get_locators_or_account('ProfilePageElements', 'addmsg')
    

    def add_worker(self, name, phone, department):
        """添加业务员"""
        self.click_new_btn()
        self.input_name(name)
        self.input_phone(phone)
        self.input_department(department)
        self.click_commit_btn()
    def alter_worker(self, name, phone,department):
        """修改业务员"""

        self.click_msssage_row()
        self.click_alter_btn()
        self.clear_name(name)
        self.input_name(name)
        self.clear_phone(phone)
        self.input_phone(phone)
        self.clear_department(department)
        self.input_department(department)
        self.click_commit_btn()

    def delete_worker(self):
        """删除业务员"""

        self.click_msssage_row()
        self.click_delete_btn()
        self.click_commit_del_btn()

    def click_new_btn(self):
        return self.click(*ProfilePage.new_worker_btn)

    def click_alter_btn(self):
        return self.click(*ProfilePage.alter_worker_btn)

    def click_delete_btn(self):
        return self.click(*ProfilePage.delete_worker_btn)

    def click_msssage_row(self):
        return self.move_to_element(*ProfilePage.item)

    def input_name(self, name):
        return self.send_keys(name,*ProfilePage.name)

    def input_phone(self, phone):
        return self.send_keys(phone,*ProfilePage.phone)

    def input_department(self, department):
        return self.send_keys(department,*ProfilePage.department)

    def clear_name(self,name):
        return self.clear(*ProfilePage.name)

    def clear_phone(self,phone):
        return self.clear(*ProfilePage.phone)

    def clear_department(self,department):
        return self.clear(*ProfilePage.department)   

    def click_commit_btn(self):
        return self.click(*ProfilePage.commit)

    def click_commit_del_btn(self):
        return self.click(*ProfilePage.commit_del)    

    def get_add_text(self):
        return self.get_element_text(*ProfilePage.add_tip)


if __name__ == '__main__':
    pass
