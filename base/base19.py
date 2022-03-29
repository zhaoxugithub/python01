'''
关键字参数

关键子参数必须在位置参数后面
*arguments:接受元组,列表,多个参数
**keywords: 接受字典类型的数组
'''


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("limbrger", "Iter", "really", a=1, b=3, c=5)

print("====" * 40)

li = [1, 2, 3, 4, 5, 6, 7]
di = {"a": 1, "b": 2, "c": 3}

cheeseshop("start", li, di)

cheeseshop("start", li, {"a": 1, "b": 2, "c": 3})
