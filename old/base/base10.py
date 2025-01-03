#!/usr/bin/env python
# -*- coding: UTF-8 -*-


'''

一个类创建的时候，就会包含一些方法，主要有以下方法：

类的专有方法：

方法	说明
__init__	构造函数，在生成对象时调用
__del__	析构函数，释放对象时使用
__repr__	打印，转换
__setitem__	按照索引赋值
__getitem__	按照索引获取值
__len__	获得长度
__cmp__	比较运算
__call__	函数调用
__add__	加运算
__sub__	减运算
__mul__	乘运算
__div__	除运算
__mod__	求余运算
__pow__	乘方
当然有些时候我们需要获取类的相关信息，我们可以使用如下的方法：

type(obj)：来获取对象的相应类型；
isinstance(obj, type)：判断对象是否为指定的 type 类型的实例；
hasattr(obj, attr)：判断对象是否具有指定属性/方法；
getattr(obj, attr[, default]) 获取属性/方法的值, 要是没有对应的属性则返回 default 值（前提是设置了 default），否则会抛出 AttributeError 异常；
setattr(obj, attr, value)：设定该属性/方法的值，类似于 obj.attr=value；
dir(obj)：可以获取相应对象的所有属性和方法名的列表：
'''


class UserInfo(object):
    def __init__(self, name, age, account):
        self.name = name
        self._age = age
        self.__account = account

    def get_account(self):
        return self.__account


if __name__ == '__main__':
    userInfo = UserInfo('两点水', 23, 347073565)
    # 打印所有属性
    print(dir(userInfo))
    # 打印构造函数中的属性
    print(userInfo.__dict__)
    print(userInfo.get_account())
    # 用于验证双下划线是否是真正的私有属性
    print(userInfo._UserInfo__account)
