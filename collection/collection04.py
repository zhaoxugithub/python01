from math import pi

'''
列表推导式
'''

squares = []
for x in range(10):
    # square x **2 是平方的意思
    squares.append(x ** 2)

print(squares)

squares = list(map(lambda x: x ** 2, range(10)))

print(squares)

squares = [x ** 2 for x in range(11)]
print(squares)

print("-" * 20)

s = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(s)

# ===上述代码等价于下面这段代码===>
ssss = (1, 2, 3, 4)
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))

print("---" * 30)

vec = [-4, -3, 0, 2, 4]
print(vec)

result2 = [x * 2 for x in vec]
print(result2)

result3 = [abs(x) for x in vec]
print(result3)

print('-' * 40)
freshfruit = ['banna   ', 'loganberr  y', '  passion fruit']

# ['banna', 'loganberr  y', 'passion fruit']
result = [weapon.strip() for weapon in freshfruit]
print(result)

result = [(x, x ** 2) for x in range(6)]
print(result)

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [num for elem in vec for num in elem]
print(result)

result = [str(round(pi, i)) for i in range(1, 6)]
print(result)
