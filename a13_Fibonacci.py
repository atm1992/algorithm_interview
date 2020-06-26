# -*- coding: UTF-8 -*-

"""
斐波那契数列。
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
f(0)=0  f(1)=1
f(2)=1  f(3)=2
f(4)=3  f(5)=5
"""


def Fibonacci(n):
    """使用一个列表来保存前两个斐波那契数。时间复杂度为O(n)"""
    res = [0, 1]
    for i in range(2, n + 1):
        res[i % 2] = res[0] + res[1]
    return res[n % 2]


if __name__ == '__main__':
    print(Fibonacci(-2))
