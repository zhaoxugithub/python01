# coding:utf-8

names = ('dewei', 'xiaomu', 'xiaowang')

names_add = names + names
names_c = names * 10

print(names_add)
print(names_c)
print('names_c length is', len(names_c))

names += ('abc',)
print(names)
names *= 10
print(names)

names_list = ['dewei', 'xiaomu']
names_list += ['xiaowang']
print(names_list)
names_list *= 5
print(names_list)

print('dewei' in names_list)
print('dewei' not in names_list)

'''
    元组不可变，列表可变，并且，元组的性能是优于列表的
'''
t1 = (1,)
print("t1 = {0}".format(t1))

t1 += (3, 4, 5)
print("t1={0}".format(t1))

# 会报错
# t1[0] = 100
# print(t1)
# t1.remove(1)

# list
list = [1, 2, 3, 4, 5]
print("list={0}".format(list))

list[0] = 1000
print("list={0}".format(list))
# 用来删除指定元素内容
list.remove(3)
print("list={0}".format(list))
