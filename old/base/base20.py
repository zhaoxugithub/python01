'''

仅限位置形参应放在 / （正斜杠）前。/ 用于在逻辑上分割仅限位置形参与其它形参.

/ 后可以是 位置或关键字 或 仅限关键字 形参.
把形参标记为 仅限关键字，表明必须以关键字参数形式传递该形参，应在参数列表中第一个 仅限关键字 形参前添加 *



'''


def standard_arg(arg):
    print(arg)


def pos_only_arg(arg, /):
    print(arg)


def kwd_only_arg(*, arg):
    print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)


print("----" * 20)
standard_arg(2)
standard_arg(arg=3)

print("----" * 20)

pos_only_arg(1)
# 报错
# pos_only_arg(arg=1)


print("----" * 20)
# 报错
# kwd_only_arg(3)
kwd_only_arg(arg=3)

print("----" * 20)
combined_example(1, 2, kwd_only=3)
combined_example(1, standard=2, kwd_only=3)
# 报错
#combined_example(pos_only=1, standard=2, kwd_only=3)
