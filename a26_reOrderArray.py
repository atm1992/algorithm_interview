# -*- coding: UTF-8 -*-

"""
调整数组顺序使奇数位于偶数前面。
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

解题思路：
"""


def reOrderArray(arr):
    if not arr or len(arr) < 1:
        return []
    n = len(arr)
    first_even = 0
    # 找到第一个偶数所在的位置
    # arr[first_even]%2==1 也可写成 arr[first_even]&1==1
    while first_even < n and arr[first_even] % 2 == 1:
        first_even += 1
    odd = first_even + 1
    while odd < n:
        if arr[odd] % 2 == 1:
            arr.insert(first_even, arr.pop(odd))
            first_even += 1
        odd += 1
    return arr


def reOrderArray_2(arr):
    return sorted(arr, key=lambda x: x % 2, reverse=True)
