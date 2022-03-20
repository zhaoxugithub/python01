import json


def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


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


if __name__ == '__main__':
    testSquare()
