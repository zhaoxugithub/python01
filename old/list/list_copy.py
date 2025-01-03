# coding:utf-8
'''
 这里注意一个问题，
    new句柄= old句柄 实际上是指向的同一个内存地址

    copy是拷贝，拷贝出来的列表和原来的时不一样的


'''
old_list = ['python', 'django', 'flask']

new_list = old_list
new_list.append('tornado')

print(new_list)
print(old_list)
print(id(new_list), id(old_list))

old_list.remove('tornado')
print(new_list, old_list)

del new_list
print(old_list)


old_list_copy = ['python', 'django', 'flask']
new_list_copy = old_list_copy.copy()

print(old_list_copy, new_list_copy)
new_list_copy.append('tornado_copy')
print(old_list_copy, new_list_copy)
print(id(old_list_copy), id(new_list_copy))

