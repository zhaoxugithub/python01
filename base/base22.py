def input_function():
    line = input("please input a word:")
    print(line)
    print(type(line))

    line_eval = eval(line)
    print(type(line_eval))


def raw_input_function():
    # line = raw_input("")
    pass


def print_function():
    '''Python两种输出值的方式: 表达式语句和 print() 函数。
    (第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用。)
    :return:
    '''
    x = "Hello"
    l = len(x)
    print("the length of %s is %d" % (x, l))

    # 指定占位符宽度（左对齐）
    print("Name:%-10s Age:%-8d Height:%-8.2f" % ("Aviad", 25, 1.83))
    # 指定占位符（若位数不够则用0填充）
    print("Name:%-10s Age:%08d Height:%08.2f" % ("Aviad", 25, 1.83))


def eval_function():
    '''
    eval函数可以实现list、dict、tuple与str之间的转化
    :return:
    '''
    a = "[[1,2], [3,4], [5,6], [7,8], [9,0]]"
    print(type(a))  # str

    b = eval(a)
    print(type(b))  # list
    print(b)


if __name__ == '__main__':
    print_function()
