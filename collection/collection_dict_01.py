def function_01():
    '''
    dict = {key1 : value1, key2 : value2 }
    注意：键必须是唯一的，但值则不必。值可以取任何数据类型，但键必须是不可变的。
    :return:
    '''
    dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
    dict2 = {'abc': 1234, 1234: 'abc'}

    name = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004',
            '五点水': '131456780005'}

    print(name['两点水'])


def function_02():
    dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
    print(dict1)
    # 新增一个键值对
    dict1['jack'] = '444444'
    print(dict1)
    # 修改键值对
    dict1['liangdianshui'] = '555555'
    print(dict1)


def function_03():
    dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333'}
    print(dict1)
    # 通过 key 值，删除对应的元素
    del dict1['twowater']
    print(dict1)
    # 删除字典中的所有元素
    dict1.clear()
    print(dict1)
    # 删除字典
    del dict1

    # UnboundLocalError: local variable 'dict1' referenced before assignment
    # print(dict1)


def function_04():
    '''
        1. dict （字典）是不允许一个键创建两次的，但是在创建 dict （字典）的时候如果出现了一个键值赋予了两次，会以最后一次赋予的值为准
        2. dict （字典）键必须不可变，可是键可以用数字，字符串或元组充当，但是就是不能使用列表
    :return:
    '''
    dict1 = {'liangdianshui': '111111', 'twowater': '222222', '两点水': '333333', 'twowater': '444444'}
    print(dict1)
    print(dict1['twowater'])

    dict1 = {'liangdianshui': '111111', 123: '222222', (123, 'tom'): '333333', 'twowater': '444444'}
    print(dict1)


def function_05():
    '''
     dict 内部存放的顺序和 key 放入的顺序是没有任何关系
    和 list 比较，dict 有以下几个特点：
    查找和插入的速度极快，不会随着key的增加而变慢
    需要占用大量的内存，内存浪费多
    而list相反：
    查找和插入的时间随着元素的增加而增加
    占用空间小，浪费内存很少
    :return:
    '''
    name = {'一点水': '131456780001', '两点水': '131456780002', '三点水': '131456780003', '四点水': '131456780004',
            '五点水': '131456780005'}
    print(len(name))

    print(str(name))

    print(type(name))

    copy_name = name.copy()
    print(copy_name)

    values = name.values()

    print(values)

    for va in values:
        print(va)

    item = name.items()
    print("item=", item)

    for en in item:
        print(en)
        print(en[0], en[1])


if __name__ == '__main__':
    function_02()
