# -*- coding: UTF-8 -*-
"""
快速排序。不稳定排序
默认使用第一个元素作为基准值，然后将数列切成两半，再递归处理。分治法
"""


def quick_sort(alist):
    if not alist or len(alist) < 2:
        return alist
    mid = alist[0]
    left_li = [x for x in alist[1:] if x <= mid]
    right_li = [x for x in alist[1:] if x > mid]
    left = quick_sort(left_li)
    right = quick_sort(right_li)
    return left + [mid] + right


if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("快速排序前：", alist)
    # 这里与之前的排序不一样，这里是返回一个排好序的新列表，原列表没有改变
    res = quick_sort(alist)
    print("快速排序后：", res)
