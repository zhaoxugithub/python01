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


def json_function4():
    '''
        [
            dict1={key1:list1,key2:list2}
            dict2={key1:str1,key2:str2}
        ]
    :return:
    '''
    list1 = [
        {'A': [1, 2, 3, 4, 5, 6], 'B': [3, 4, 5, 6, 7]},
        {'C': '123', 'D': '234'}
    ]

    # 讲数据写入文件
    file = open('json_demo.json', 'w')
    for i in list1:
        # json_i是一个str
        json_i = json.dumps(i)
        file.write(json_i + '\n')
    file.close()

    # 从文件中读取数据
    get_data = []
    with open('json_demo.json', 'r') as f:
        #  读取数据并分割，最后一个为空，所以去除
        # [:-1] 表示从开始到倒数第二个
        new_list = f.read().split('\n')[:-1]
        print("new_list={}".format(new_list))
        for x in new_list:
            # 读取x，x是一个str,json_x 是一个dict
            json_x = json.loads(x)
            print(type(json_x))
            get_data.append(json_x)
    f.close()

    print(f'原始数据位:{list1}')
    print(f'结果数据为:{get_data}')


def json_function5():
    # 字典
    dic = {'name': 'dgw', 'sex': 'female', 'age': 30, 'grade': [{"语文": 96}, {'数学': 99}]}
    print(dic)

    # json 数据是双引号
    '''
        ensure_ascii=False 表示[{"语文": 96}, {"数学": 99}]}
        ensure_ascii=True  表示[{"\u8bed\u6587": 96}, {"\u6570\u5b66": 99}]}
    '''
    json_dic = json.dumps(dic, ensure_ascii=False)
    print("json_dic={},type={}".format(json_dic, type(json_dic)))

    # 对json_dic 数据进行转义
    json_dic_escape = json.dumps(json_dic, ensure_ascii=False)
    print("json_dic_escape={},type={}".format(json_dic_escape, type(json_dic_escape)))

    # 对dic数据中的某个字段进行单独转义
    dic['grade'] = json.dumps(dic['grade'], ensure_ascii=False)
    json_dic_escape2 = json.dumps(json.dumps(dic, ensure_ascii=False), ensure_ascii=False)
    print("json_dic_escape2={}".format(json_dic_escape2))

    # 对json_dic_escape2 数据进行转义解码
    json_dic_escape_decode = json.loads(json_dic_escape2)
    print("json_dic_escape_decode={}".format(json_dic_escape_decode))

    with open('text.txt', 'a', encoding='utf-8') as f:
        f.write(str(dic) + '\n')
        f.write(json_dic + '\n')
        f.write(json_dic_escape + '\n')
        f.write(json_dic_escape2 + '\n')
        f.write(json_dic_escape_decode + '\n')


if __name__ == '__main__':
    # math_function()
    json_function5()
