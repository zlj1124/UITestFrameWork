'''
@Descripttion: 
@Author: zlj
@Date: 2019-12-05 11:05:13
'''

import pytest
from data.worker_data import ProfileData
from util.db import DbConnect

local_db = DbConnect('jing5DB')


class Testupload_file(object):
    """上传文件"""
 

    # @pytest.mark.skip
    # @pytest.mark.parametrize('name,phone,department, expect', add_success_data)
    def test_a_uploadfile(self, login, refresh_page):
        """验证上传文件"""
        
        home_page = login[1]
        truck_page= login[2]
        home_page.select_menu(menu="truck")
        truck_page.uploadfile()
        actual = truck_page.get_uploadmsg()
        print("actual:{}".format(actual))
       
        # assert expect in actual, "添加成功, 断言失败"






if __name__ == '__main__':
    pytest.main(['-s', 'test_uploadfile.py'])
