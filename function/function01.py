# -*-coding:utf-8-*-
# !/usr/bin/env python3

def ask_on(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


i = 5


def f(arg=i):
    print(arg)

f()


