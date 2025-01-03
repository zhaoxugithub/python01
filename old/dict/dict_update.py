# coding:utf-8

user = {'username': 'dewei', 'age': 33, 'height': 177}
xiaomu = {'username': '小慕', 'age': 10, 'top': 175, 'sex': '男'}

# 会把xiaomu种的key与user相同的key更新到user里面
user.update(xiaomu)
print(user)

value = user.setdefault('username', 'xiaoyun')
value = user.setdefault('birthday', '2020-1-1')
print(user, value)

# user['top'] = 174
#
# print(user)
# user['username'] = '小慕'
# print(user)
# user['top'] = 175
# user['age'] = 10
# print(user)
