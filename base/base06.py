'''

多继承有一点需要注意的：若是父类中有相同的方法名，而在子类使用时未指定，
python 在圆括号中父类的顺序，从左至右搜索 ， 即方法在子类中未找到时，从左到右查找父类中是否包含方法。
'''


class UserInfo(object):
    lv = 5

    def __init__(self, name, age, account):
        self.name = name
        self.age = age
        self.account = account

    def get_account(self):
        return self.account


class UserInfo2(UserInfo):
    pass


if __name__ == '__main__':
    ui2 = UserInfo2("zx", 20, 444444)
    print(ui2.get_account())
