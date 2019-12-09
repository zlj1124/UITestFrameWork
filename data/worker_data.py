
class ProfileData(object):
    """添加业务员测试数据"""

    add_worker_success = [
        (
            "linux",
            "13691579841",
            "市场营销",
            "添加成功"
        )
    ]
    add_worker_fail = [
        (
            "linux2",
            "13691579841",
            "行政管理",
            "电话: 该手机号已经存在，不能创建"
        )
    ]    
    alter_worker_success = [
        (
            "linux1",
            "13691579842",
            "行政管理",
            "修改成功"
        )    
    ]
    delete_worker_success = [
        (
            "删除成功"
        )    
    ]


if __name__ == '__main__':
    pass
