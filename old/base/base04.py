class B():
    var1 = "hello world"

    def func(self):
        print("vvvvvvvvvvvvvvvvvv")


def newFunc(self):
    print("new Func")


if __name__ == '__main__':
    b = B()
    print(b.var1)
    b.func()

    # 通过类名.变量名 可以修改所有实例变量
    B.var1 = "fffff"
    print(b.var1)

    # 通过类名.方法名 = new的方法名，可以重写类的方法
    B.func = newFunc
    b.func()

    # 下面的这种方式就会报错
    # TypeError: newFunc() missing 1 required positional argument: 'self'
    b.func = newFunc
    b.func()
