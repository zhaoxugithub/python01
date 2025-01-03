# coding:utf-8
'''

    主要讲的是 strip的用法和lstrip以及 rstrip

'''
info = '    my name is dewei    '
new_info = info.strip()
print('.' + new_info + '.')

info_01 = 'my name is dewei'
new_info_01 = info_01.strip(info_01)
print(new_info_01)
print(len(new_info_01))

new_str = 'abcde'
print(new_str.lstrip('a'))
print(new_str.rstrip('e'))
