# -*- coding: UTF-8 -*-
"""
和为S的两个数字。
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。

解题思路：使用双指针。一个指向较小的值，从前往后遍历；另一个指向较大的值，从后往前遍历。若这两个值的和为S，则得到所求结果。
在指针的移动过程中，若和小于S，则移动较小的指针，使得和变大；若和大于S，则移动较大的指针，使得和变小。
为什么找到了第一组结果就可以直接返回？
因为原始数组是递增有序的，而对于和相同的两组数，越靠近边缘的乘积越小，越靠近中间的乘积则越大。
以和为10为例，4*6 > 3*7 > 2*8 > 1*9
"""


def FindNumbersWithSum(array, tsum):
    if not array or len(array) < 2 or not tsum:
        return []
    front, rear = 0, len(array) - 1
    # 因为要求的是两个数，所以 front 不能等于 rear
    while front < rear:
        cur_sum = array[front] + array[rear]
        if cur_sum < tsum:
            front += 1
        elif cur_sum > tsum:
            rear -= 1
        else:
            return [array[front], array[rear]]
    return []
