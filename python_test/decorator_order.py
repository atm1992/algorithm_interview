# -*- coding: UTF-8 -*-
"""
一个函数被多个装饰器装饰时，验证各个装饰器的执行顺序
"""


def decorator_a(func):
    print("get in decorator_a")

    def inner_a(*args, **kwargs):
        print("get in inner_a")
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    print("get in decorator_b")

    def inner_b(*args, **kwargs):
        print("get in inner_b")
        return func(*args, **kwargs)

    return inner_b

# 按从下至上的顺序依次调用装饰器decorator_a、decorator_b
# 虽然有多个装饰器，但f(x)函数体内的语句只会执行一次
# 在Python解释器执行f(1)之前，实际上已经依次调用了decorator_a、decorator_b，此时的函数f其实是inner_b，
# 所以当执行f(1)时，会先执行inner_b，然后在inner_b的内部调用inner_a，最后在inner_a的内部调用最初的f
@decorator_b
@decorator_a
def f(x):
    print("get in f")
    return x * 2


if __name__ == '__main__':
    print(f(1))
