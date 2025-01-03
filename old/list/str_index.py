# coding:utf-8

name = 'dewei'
new_name = name[::-1]
print(new_name)

print(new_name)
# index 方法如果找不到会报错
# result = new_name.index('wei')
find_result = new_name.find('wei')
print("find_result={0}".format(find_result))
# print(result)
