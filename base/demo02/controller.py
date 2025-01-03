# coding:utf-8


def test01():
    while True:
        username = input("please input username:")
        password = input("please input password:")
        if username == 'admin' and password == '123456':
            print("success!")
            break
        else:
            print("error!")


if __name__ == '__main__':
    test01()
