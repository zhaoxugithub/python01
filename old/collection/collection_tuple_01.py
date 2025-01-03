'''
tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。
    也就是说元组（tuple）是不可变的，那么不可变是指什么意思呢？

元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，
也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
'''


def tuple_function01():
    tuple1 = ('两点水', 'twowter', 'liangdianshui', 123, 456)
    tuple2 = '两点水', 'twowter', 'liangdianshui', 123, 456
    tuple3 = ()

    print(tuple1)
    # 这种是tuple
    tuple4 = (123,)

    # 这种创建是一个具体的元素
    tuple5 = (222)
    pass


def tuple_function02():
    name1 = ('一点水', '两点水', '三点水', '四点水', '五点水')

    name2 = ('1点水', '2点水', '3点水', '4点水', '5点水')
    print("name1 length=", len(name1))

    print("merge name1 and name2", name1 + name2)

    print("copy name1", name1 * 2)

    print("一点水" in name1)

    print("name2 max", max(name2))

    print("name2 min", min(name2))

    list1 = [1, 2, 3, 4, 5]
    print("list to tuple", tuple(list1))


if __name__ == '__main__':
    tuple_function01()
