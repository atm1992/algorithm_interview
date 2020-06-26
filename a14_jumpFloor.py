# -*- coding: UTF-8 -*-
"""
跳台阶。
一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。

跳n级台阶可分为两种情况：第一步跳1级（然后跳n-1级）、第一步跳2级（然后跳n-2级）
f(n)=f(n-1)+f(n-2)          其实就是斐波那契数列
f(1)=1  f(2)=2
f(3)=3  f(4)=5
"""


# number 为台阶数
def jumpFloor(number):
    """使用一个列表来保存f(n-1)、f(n-2)的结果。时间复杂度为O(n)"""
    if number < 1:
        return 0
    # 使用一个列表来保存台阶数number为1、2时的情况
    res = [1, 2]
    for i in range(3, number + 1):
        res[(i + 1) % 2] = res[0] + res[1]
    return res[(number + 1) % 2]


if __name__ == '__main__':
    print(jumpFloor(10))
