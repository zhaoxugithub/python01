# def foo(name, **kwds):
#     return "name2" in kwds
#
#
# foo(1, {"name2": 2})


def toEE(num):
    for i in reversed(range(31)):
        if (1 << i) & num == 0:
            print(0, end="")
        else:
            print(1, end="")


if __name__ == '__main__':
    toEE(8)
