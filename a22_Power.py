# -*- coding: UTF-8 -*-

"""
数值的整数次方。
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0

解题思路：因为指数exponent是整数，因此可以使用递归将指数每次都对半切，直到指数为0或1，这样可以减小计算量
"""


def Power(base, exponent):
    try:
        res = power_value(base, abs(exponent))
        if exponent < 0:
            res = 1.0 / res
    except Exception:
        print("Error: base is zero")
        return
    return res


def power_value(base, exponent):
    # 递归终止条件
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    res = power_value(base, exponent >> 1)
    res *= res
    if exponent % 2 == 1:
        res *= base
    return res


if __name__ == '__main__':
    print(Power(0, 5))
