
import pytest
from util.db import DbConnect
from data.worker_data import ProfileData
local_db = DbConnect('jing5DB')


class TestAddworker(object):
    """添加业务员"""
    worker_data = ProfileData
    add_success_data = worker_data.add_worker_success
    add_fail_data = worker_data.add_worker_fail
    alter_success_data = worker_data.alter_worker_success
    delete_success_data = worker_data.delete_worker_success

    # @pytest.mark.skip
    @pytest.mark.parametrize('name,phone,department, expect', add_success_data)
    def test_a_add_success(self, login, refresh_page, name,phone, department, expect):
        """验证添加业务员"""
        
        home_page = login[1]
        profile_page = login[2]
        print("login[1]:{},login[2]:{}".format(login[1],login[2]))

        home_page.select_menu(menu="settings")
        profile_page.add_worker(name, phone, department)
        actual = profile_page.get_add_text()
        print("expect:{},actual:{}".format(expect,actual))
       
        assert expect in actual, "添加成功, 断言失败"

    # @pytest.mark.skip
    @pytest.mark.parametrize('name, phone, department, expect', add_fail_data)
    def test_b_add_fail(self, login, refresh_page, name, phone, department, expect):
        """验证添加业务员唯一"""
        # home_page = login[1]
        profile_page = login[2]
        # home_page.select_menu(menu="settings")
        profile_page.add_worker(name, phone, department)
        actual = profile_page.get_add_text()
        expect='{1}{0}{1}'.format(expect,'"')
        print("expect:{},actual:{}".format(expect,actual))
        assert actual in expect, "添加失败, 断言失败"

    # @pytest.mark.skip
    @pytest.mark.parametrize('name, phone, department, expect',alter_success_data)
    def test_c_alter_success(self, login, refresh_page, name, phone, department, expect):
        """验证修改业务员"""
        # home_page = login[1]
        profile_page = login[2]
        # home_page.select_menu(menu="settings")
        profile_page.alter_worker(name, phone, department)
        actual = profile_page.get_add_text()
        print("expect:{},actual:{}".format(expect,actual))
        assert actual == expect, "修改成功, 断言失败"

    @pytest.mark.parametrize('expect',delete_success_data)
    def test_d_delete_success(self, login, refresh_page, expect):
        """验证删除业务员"""
        # home_page = login[1]
        profile_page = login[2]
        # home_page.select_menu(menu="settings")
        profile_page.delete_worker()
        actual = profile_page.get_add_text()
        print("expect:{},actual:{}".format(expect,actual))
        assert actual == expect, "删除成功, 断言失败"

    # def teardown_class(self):
    #     '''通过数据库保持数据一致性'''
    #     local_db.delete_sql("owl_profile",'name','linux1')
    #     local_db.close_conn()
        



if __name__ == '__main__':
    pytest.main(['-s', 'test_ProfileCase.py'])
