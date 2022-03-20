class C():
    def __init__(self, str):
        print("创建对象实例构造方法初始化...")
        print(str)

    def __del__(self):
        print("销毁对象实例...")


if __name__ == '__main__':
    c = C("哈哈啊哈")
    del c
