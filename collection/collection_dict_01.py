# https://www.bookstack.cn/read/52fhy-python/f6ab350838a65d6d.md
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


def dict_function06():
    dic = {'name': 'Zara', 'age': 7, 'class': 'First'}

    # 移除单个元素
    del dic['name']
    # 移除所有的元素
    dic.clear()
    print(dic)
    # 删除字典
    del dic

    # print(dic) 会报错，因为dic不存在


def dict_function07():
    dic1 = {'name': 'Zara', 'age': 7, 'class': 'First'}
    dic2 = {'name': 'Zara', 'age': 7, 'class': 'First'}

    # res1 = cmp(dic1, dic2)
    # print("cmp ={}".format(res1))

    print("len ={}".format(len(dic1)))

    print("str={}".format(str(dic2)))

    print("type={}".format(type(dic1)))

    # dic1.clear()

    dict.clear(dic1)
    print(dic1)

    dict2_copy = dict.copy(dic2)
    print("dict2_copy={}".format(dict2_copy))

    dict2_keys = dict.fromkeys(dic2)
    print("dict2_keys={}".format(dict2_keys))

    # 取值,如果存在name这个key,就取出来，不然就取no element
    name_value = dic2.get("name", "no element")
    print("name_value={}".format(name_value))

    g_value = dic2.get("g", "no element")
    print("g_element = {}".format(g_value))

    # 判断是否存在key
    res = "name" in dic2
    print("res = {}".format(res))

    # 遍历
    for k, v in dic2.items():
        print("key={},value={}".format(k, v))

    values_list = dic2.values()
    key_list = dic2.keys()
    print("key_list={},value_list={}".format(key_list, values_list))

    dic2.setdefault("ggg", "ggg_value")
    print("dic2={}".format(dic2))

    dic2.setdefault("name", "zhaoxu")
    print("dict2={}".format(dic2))

    dic3 = {"height": 177, "weight": 66}
    # 把dic3追加到dic2中
    dic2.update(dic3)
    print("dic_new={}".format(dic2))


if __name__ == '__main__':
    dict_function07()
