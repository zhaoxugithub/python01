import base12

'''
在 Python 函数中，如果一个函数调用了其他函数完成一项功能，我们称这个函数为主函数，如果一个函数没有调用其他函数，我们称这种函数为非主函数。主模块和非主模块的定义也类似，如果一个模块被直接使用，而没有被别人调用，我们称这个模块为主模块，如果一个模块被别人调用，我们称这个模块为非主模块。

仔细观察的人，基本会发现，每一个包目录下面都会有一个 __init__.py 的文件，为什么呢？

因为这个文件是必须的，否则，Python 就把这个目录当成普通目录，而不是一个包 。 __init__.py 可以是空文件，也可以有Python代码，因为 __init__.py 本身就是一个模块，而它对应的模块名就是它的包名。

'''