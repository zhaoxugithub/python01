import json
import math
import cmath


# https://blog.csdn.net/weixin_44799217/article/details/112256220

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

    '''
    转换标志：-表示左对齐；+表示在转换值之前要加上正负号；""（空白字符）表示正数之前保留空格；0表示转换值若位数不够则用0填充。
    '''
    # 指定占位符宽度（左对齐）
    print("Name:%-10s Age:%-8d Height:%-8.2f" % ("Aviad", 25, 1.83))
    # 指定占位符（若位数不够则用0填充）
    print("Name:%-10s Age:%08d Height:%08.2f" % ("Aviad225555522", 25, 1.83))

    print("His height is %f m" % (1.83))
    # 保留两位小数
    print("His height is %.2f m" % (1.83))

    print("The String is %2.s" % ("abcd"))
    # 用*从后面的元组中读取字段宽度或精度，第1个参数是精度
    print("His height is %.*f m" % (2, 1.833))


def prn_obj(obj):
    print(', '.join(['%s:%s' % item for item in obj.__dict__.items()]))


def math_function():
    li = [1, 2, 3, 4]
    print(str(li))  # 把值转换为字符串
    print(repr(li))  # 返回值的字符串标示形式

    number = -10000
    print(abs(number))  # 返回数字的绝对值

    print(cmath.sqrt(number))  # 返回平方根，也可以应用于负数

    f = 100
    print(float(f))  # 把字符串和数字转换为浮点数
    # help()  # 提供交互式帮助
    input("please input ")  # 获取用户输入

    i = 100.455
    print(int(i))  # 把字符串和数字转换为整数
    print(math.ceil(i))  # 返回数的上入整数，返回值的类型为浮点数
    print(math.floor(i))  # 返回数的下舍整数，返回值的类型为浮点数
    print(math.sqrt(i))  # 返回平方根不适用于负数

    x = 10
    y = 2
    print(pow(x, y[.2]))  # 返回X的y次幂（有z则对z取模）
    round(i[.2])  # 根据给定的精度对数字进行四舍五入

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


def json_function():
    li = [1, 2, 3, 4]
    li_to_json = json.dumps(li)
    print(li_to_json)

    di = {"a": 1, "b": 2, "c": 3, "d": 4}
    print(di)
    print(di["a"])

    di_to_json = json.dumps(di)
    print(di_to_json)
    print(di_to_json[0])


def json_function2():
    # 定义一个字典
    data = {'name': 'nick',
            'age': 12}

    # data_to_json 是一个str
    data_to_json = json.dumps(data)
    print(data_to_json)
    print("data_to_json type={},data type={}".format(type(data_to_json), type(data)))


def json_function3():
    dict1 = {'A': 'a', 'B': 'b', 'C': 'c'}
    print(type(dict1))
    print(dict1)

    #  python编码为json类型，json.dumps()
    en_json = json.dumps(dict1)
    print(type(en_json))
    print(en_json)

    #  json解码为python类型， json.loads(),en_json是一个字符串
    de_json = json.loads(en_json)
    print(type(de_json))
    print(de_json)

    #  eval()解析json
    dict2 = {'X': 'x', 'Y': 'y', 'Z': 'z'}
    en_json = json.dumps(dict2)  # en_json 是一个字符串
    de_json = eval(en_json)  # de_json 是一个dict
    print(type(de_json))
    print(de_json)


if __name__ == '__main__':
    # math_function()
    json_function3()
