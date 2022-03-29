# 默认值为5
i = 5

def f(args=i):
    print(args)

if __name__ == '__main__':
    i = 6
    f()