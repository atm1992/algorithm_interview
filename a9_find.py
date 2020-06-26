# -*- coding: UTF-8 -*-
"""
二维数组中的查找。
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def find(target, arr):
    """利用 每行从左到右递增、每列从上到下递增 的特性，减少扫描、比较次数，从左上角开始比较。时间复杂度为O(n)"""
    row = 0
    col = len(arr[0]) - 1
    row_total = len(arr)
    while row < row_total and col >= 0:
        val = arr[row][col]
        if val == target:
            return True
        elif val > target:
            col -= 1
        else:
            row += 1
    return False
