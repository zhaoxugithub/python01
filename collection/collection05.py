'''
嵌套的列表推导式
'''
matrix = [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12],
]

print(matrix)

result = [[row[i] for row in matrix] for i in range(4)]
print(result)

# 等价 ==>
transposed = []
for i in range(4):
    print(i)
    transposed.append([row[i] for row in matrix])

print(transposed)