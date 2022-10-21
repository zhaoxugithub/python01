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
    t1 = [1, 2, 3, 4, 5, 2]
    print("list length =", len(t1))

    print("max is = ", max(t1))

    print("min is = ", min(t1))

    print("tuple to list = ", list((2, 4, 5, 6)))

    t1.append(6)
    print("add element is =", t1)

    print("ele appearance count = ", t1.count(2))

    t1.extend([9, 10, 11])
    print("add one list to another list= ", t1)

    print("index of ele=", t1.index(10))

    t1.insert(2, 111)
    print("insert ele in index=", t1)

    # 默认移除的是最后一个元素
    print("pop last ele=", t1.pop(), "t1=", t1)

    # 移除下标为2的元素
    print("pop ele = ", t1.pop(2), "t1=", t1)

    # 移除值为10的元素
    print("remove ele = ", t1.remove(10), "t1=", t1)

    print("reverse =", t1.reverse(), "t1 = ", t1)

    print("sort = ", t1.sort(), "t1=", t1)


def list_function3():
    pass


def list_function4():
    pass


def list_function5():
    pass


if __name__ == '__main__':
    list_function2()
