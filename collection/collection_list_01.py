# 申明list
name = ['一点水', '两点水', '三点水', '四点水', '五点水']


def get_from_list():
    print(name[1])
    print(name[0:2])
    print(name[:2])
    print(name[:])
    print(name[1:2])
    print(name[0:3])

    print("-------------")
    name.append("六点水")
    print(name)

    print("======")
    del name[2]
    print(name)


def list_function1():
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]
    print(len(l1))
    print(l1 + l2)

    print(['Hi!'] * 4)

    print(3 in l2)

    for x in [1, 2, 3]: print(x)


def list_function2():
    pass


def list_function3():
    pass


def list_function4():
    pass


def list_function5():
    pass


if __name__ == '__main__':
    list_function1()
