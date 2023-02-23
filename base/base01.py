# -*-coding:utf-8-*-
# !/usr/bin/env python3

'''
第一行注释是为了告诉 Linux/OS X 系统，这是一个 Python 可执行程序，Windows 系统会忽略这个注释；
第二行注释是为了告诉 Python 解释器，按照 UTF-8 编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
'''

# -*- coding: utf-8 -*-
import json


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b
    return a, b

# 1 1
# # 引用函数
# for x in fibon(10):
#     print(x, end=' ')


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


'''
结果没有问题，但有经验的开发者会指出，直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
因为 fab 函数返回 None，其他函数无法获得该函数生成的数列。要提高 fab 函数的可复用性，最好不要直接打印出数列，而是返回一个 List。以下是 fab 函数改写后的第二个版本：
'''


def fab2(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L


def iterFab02():
    li = [i for i in fab2(5)]
    for ee in li:
        print(ee)


def iterFab01():
    li = [i for i in fab2(5)]
    iters = iter(li)
    print(iters)


def square():
    for x in range(4):
        yield x ** 2


def testSquare():
    # 返回的是一个迭代器函数
    sq = square()
    for e in sq:
        print(e)


# 和testSquare 是等价的
def testSquare2():
    sq2 = square().__iter__()
    try:
        while True:
            value = next(sq2)
            print(value)
    except:
        print("error")


def testMath():
    # 小数
    print(10 / 2)
    # 取整
    print(10 // 2)
    # 取余
    print(10 % 2)

    print("--------------")

    print(11 / 2)

    # 取整
    print(11 // 2)
    print(11 % 2)


def base_data_type_traction():
    '''
     Python 3 里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
    :return:

    int(x [,base ])	将x转换为一个整数
    float(x )	将x转换到一个浮点数
    complex(real [,imag ])	创建一个复数
    str(x )	将对象 x 转换为字符串
    repr(x )	将对象 x 转换为表达式字符串
    eval(str )	用来计算在字符串中的有效 Python 表达式,并返回一个对象
    tuple(s )	将序列 s 转换为一个元组
    list(s )	将序列 s 转换为一个列表
    chr(x )	将一个整数转换为一个字符
    unichr(x )	将一个整数转换为 Unicode 字符
    ord(x )	将一个字符转换为它的整数值
    hex(x )	将一个整数转换为一个十六进制字符串
    oct(x )	将一个整数转换为一个八进制字符串

    '''

    x = 10

    print(int(x))

    print(float(x))

    # print(compileall[x,])

    print(str(x))

    print(repr("22222222"))

    print("tuple={}", tuple([2, 3, 4]))
    print("list={}", list({2, 3, 4, 5}))

    print("char=", chr(x))
    print(ord(chr(x)))

    pass


def repr_function():
    s = "hello,world!"
    print(str(s))

    rs = repr(s)
    rs.split(rs)
    print(repr(s))

    print("-----")
    s1 = "hello world"

    # 将常用字符串转变成表达式字符串
    # 什么是表达式字符串，就是计算机能够识别的
    rp = repr(s1)
    print(rp)

    print(eval(rp))


if __name__ == '__main__':
    # base_data_type_traction()
    a = fibon(10)
    print(a)
