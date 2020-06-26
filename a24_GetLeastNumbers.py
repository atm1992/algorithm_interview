# -*- coding: UTF-8 -*-
"""
最小的K个数。
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

解题思路：若数据量较小且数据不变，则可先完全排序，然后取前k个；若数据量很大或者是流数据，则可使用大小为K的最大堆。
方法一：快速排序。不稳定排序，该方法会修改原始数组
方法二：堆排序。维护一个大小为K的最大堆，注意是最大堆，而不是最小堆。遍历原始数组时，若当前元素小于堆顶元素，则将堆顶元素替换为当前元素，并调整最大堆

注意：二叉堆虽然是一颗完全二叉树，但二叉堆并不是使用链式存储，而是采用的顺序存储，即 二叉堆的所有节点都存储在数组当中。
因为没有左右指针，因此二叉堆通过计算数组下标来定位左右孩子，数组下标从0开始，即 根节点的下标为0
"""


def GetLeastNumbers(tin, k):
    if not tin or k > len(tin) or k <= 0:
        return []
    tin = quick_sort(tin)
    return tin[:k]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[0]
    left = quick_sort([x for x in arr[1:] if x <= mid])
    right = quick_sort([x for x in arr[1:] if x > mid])
    return left + [mid] + right
