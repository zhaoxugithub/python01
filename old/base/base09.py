'''
多态
'''


class User(object):
    def __init__(self, name):
        self.name = name

    def printUser(self):
        print('Hello !' + self.name)


class UserVip(User):
    def printUser(self):
        print('hello ! vip' + self.name)


class UserGeneral(User):
    def printUser(self):
        print('hello ! generator' + self.name)


def printfUserInfo(user):
    print(user.printUser())


if __name__ == '__main__':
    uv = UserVip("vip")
    printfUserInfo(uv)

    ug = UserGeneral("general")
    printfUserInfo(ug)
