def list_function1():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print(fruits)

    print("-" * 20)
    result1 = fruits.count('apple')
    print(f'count apple is {result1}')

    print("-" * 20)
    result2 = fruits.count('tangerine')
    print(f'count tangerine is {result2} ')

    print("-" * 20)
    result3 = fruits.index('banana')
    print(f'banana index is {result3}')

    print("-" * 20)
    result4 = fruits.index('banana', 4)  # 从下标4开始（包括4）
    print(f'banana index of 4 is {result4}')

    print("-" * 20)
    result5 = fruits.reverse()
    print(f'fruits reverse is {result5}')
    print(f'fruits reverse is {fruits} ')

    print("-" * 20)

    fruits.append('grape')
    print(f'fruits append grape is {fruits}')

    print("-" * 20)

    fruits.sort()
    print(f"fruits sort is {fruits}")
    print("-" * 20)

    fruits.pop()
    print(f'fruits pop is {fruits}')

    # 在指定位置进行添加
    fruits.insert(3, "sss")
    print("fruits={}".format(fruits))
    # 添加一个列表
    exrta = [3, 4, 5, 6]
    fruits.extend(exrta)
    print("fruits={}".format(fruits))

    res = max(exrta)
    print(res)


if __name__ == '__main__':
    pass
