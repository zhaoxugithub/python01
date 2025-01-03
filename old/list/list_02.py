# coding:utf-8

squares = [1, 4, 9, 16, 25]
print(squares)

print(squares[0])
print(squares[-1])
print(squares[-3:])

# l1 和 squares 指向指向同一个对象
l1 = squares[-3:]
l1.append(36)
print(squares, l1)

squares += [49, 64, 81, 100]
print(squares)

cubes = [1, 8, 27, 65, 125]
print(cubes)
