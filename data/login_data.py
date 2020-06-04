

class LoginData(object):
    """用户登录测试数据"""

    login_success_data = [
        (
            "10086",
            "10086",
            "登录成功"
        )
    ]

    login_fail_data = [
        (
            "10086",
            "",
            "请输入密码"
        ),
        (
            "",
            "10086",
            "请输入账号"
        ),
    ]


if __name__ == '__main__':
    pass
