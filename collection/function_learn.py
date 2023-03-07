'''
    主要学习Python中的函数使用
            必选参数：fun(name, age)
            默认参数：fun(name='yjc', age=18)
            可变参数：fun(*args)
            关键字参数：fun(name, age, **kw)
            命名关键字参数：fun(name, age, *, city)
'''


# 必选参数
def print_me(str):
    print(str)
    return


# --------------------------------------------------

# 默认参数

def print_info(name, age=35):
    '''打印任何传入的字符串'''
    print("Name: ", name)
    print("Age ", age)
    return


# --------------------------------------------------


# 可变参数
def function_name(*nums):
    sum_total = 0
    for n in nums:
        sum_total = sum_total + n * n


def function_name_test():
    res = function_name(2, 3)
    print("res:", res)
    print("可变参数是一个列表:", function_name(*[2, 3, 4, 5]))
    print("可变参数是一个set:", function_name(*{2, 3, 4, 5, 6}))
    print("可变参数是一个元组:", function_name(*(4, 5, 6, 7)))


# --------------------------------------------------

# 关键字参数：
def function_kw(name, age, **kw):
    '''
    这里name, age是必须的，kw可选，意味着第三个参数开始我们可以传入任意个数的关键字参数：
    kw实际上是dict
    关键字参数kw获得的dict是param的一份拷贝，对kw的改动不会影响到函数外的param。
    '''
    print("name={},age={},kw={}".format(name, age, kw))


def function_kw_test():
    function_kw(name="name1", age="age1", city="bj")
    function_kw("name2", "age2", **{"city": "bj", "job": "Engineer"})


# --------------------------------------------------


# 命令关键字参数
def function_kw_name(name, age, *, city, job):
    '''
    和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
    :return:
    '''
    print("name={},age={},city={},job={}".format(name, age, city, job))


def function_kw_name_test():
    function_kw_name("name11", age=30, city='sh', job='it')
    function_kw_name("name11", age=30, city={"k1": "v1"}, job="teacher")


# --------------------------------------------------


# 可变参数+命名关键字参数
def function_kw_all(name, age, *args, city, job):
    print("name={},age={},args={},city={},job={}".format(name, age, args, city, job))


def function_kw_all_test():
    function_kw_all("name1", 30, *[1, 2, 3, 4], city="sh", job='it')


# --------------------------------------------------

if __name__ == '__main__':
    function_kw_test()
    function_kw_name_test()
    function_kw_all_test()
