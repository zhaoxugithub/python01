class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def get_account(self):
        return self.account

    @classmethod
    def get_name(cls):
        return cls.lv

    def get_age(self):
        return self.age


class UserInfo2(UserInfo):
    def __init__(self, name, age, account, sex):
        super(UserInfo2, self).__init__(name, age, account)
        self.sex = sex


if __name__ == '__main__':
    ui2 = UserInfo2("zx", 20, "2000", "男")
    # 打印这个对象的所有属性
    print(dir(ui2))
    # 打印构造函数里面的所有属性
    print(ui2.__dict__)
    print(ui2.get_name())
