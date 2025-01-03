# coding:utf-8

def test1():
    a = 321
    b = 12
    print(a + b)  # 333
    print(a - b)  # 309
    print(a * b)  # 3852
    print(a / b)  # 26.75


def test2():
    a = 100
    b = 12.345
    c = 1 + 5j
    d = 'hello, world'
    e = True
    print(type(a))    # <class 'int'>
    print(type(b))    # <class 'float'>
    print(type(c))    # <class 'complex'>
    print(type(d))    # <class 'str'>
    print(type(e))    # <class 'bool'>

def test3():
    a = int(input('a = '))
    b = int(input('b = '))
    print('%d + %d = %d' % (a, b, a + b))
    print('%d - %d = %d' % (a, b, a - b))
    print('%d * %d = %d' % (a, b, a * b))
    print('%d / %d = %f' % (a, b, a / b))
    print('%d // %d = %d' % (a, b, a // b))
    print('%d %% %d = %d' % (a, b, a % b))
    print('%d ** %d = %d' % (a, b, a ** b))


if __name__ == '__main__':
    test1()
    test2()
    test3()
