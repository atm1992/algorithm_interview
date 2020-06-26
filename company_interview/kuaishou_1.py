# -*- coding: UTF-8 -*-
"""
计算两个正数相加时的进位次数。

问题分析：
1、一个正数加上一个正数，若进位为0，并且有一个数为0，则跳出循环
2、一个负数加上另一个负数，可看做是两个正数相加，然后前面取负号，因此进位次数等同于两个正数相加
3、一个正数加上一个负数，相当于减法，减法没有进位，只有借位，因此进位次数为0
"""


def count_carry(m, n):
    carry = 0
    count = 0
    while m > 0 or n > 0:
        carry = (m % 10 + n % 10 + carry) // 10
        if carry > 0:
            count += 1
        elif m == 0 or n == 0:
            break
        m //= 10
        n //= 10
    return count + 1 if carry > 0 else count


if __name__ == '__main__':
    print(count_carry(999, 1))
