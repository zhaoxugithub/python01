'''



'''


def f(a, l=[]):
    l.append(a)
    return l


'''
[1]
[1, 2]
[1, 2, 3]

原因是：def f(a,l =[] )  
 ===>
   
     l = [] 
    def f(a):

相当于在函数外 单独设置一个变量      

'''


def f2(a, l=None):
    if l is None:
        l = []
    l.append(a)
    return l


if __name__ == '__main__':
    print(f2(1))
    print(f2(2))
    print(f2(3))
