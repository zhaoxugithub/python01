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


