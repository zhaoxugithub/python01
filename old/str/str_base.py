# coding:utf-8

str1 = 'doesn\'t'
str2 = "doesn't"

print(f"str ={str1}, result = {str1 == str2}")

str3 = '"Yes," they said.'
str4 = "\"Yes,\" they said."
print(f"str ={str3}, result = {str3 == str4}")

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 会自动将两个字符串连接在一起， 但是不能 有变量 和字面量 合在一起
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# str 的字符操作
word = "Python"
print(f"word[0] = {word[0]}")
print(word[0])
print(word[5])

print(word[-1])
print(word[-2])
print(word[-6])

print(word[0:2])
print(word[2:5])
