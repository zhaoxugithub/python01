class A():
    var1 = "hello"
    var2 = "world"
    var3 = "java"

    def show(self):
        print(A.var3)

    @classmethod
    def show2(cls):
        print(cls.var3)

    def show3(self):
        print(self.var3)


if __name__ == '__main__':
    # if __naTypeError: show() missing 1 required positional argument: 'self'me__ == '__main__':
    # 如要保证正确，只需要在show，show2,show3 方法上添加注解；    @classmethod
    # A.show()
    # # A.show2()
    # A.show3()

    A.show2()

    a = A()
    a.show()
    a.show2()
    a.show3()
