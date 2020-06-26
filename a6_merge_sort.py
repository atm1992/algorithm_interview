# -*- coding: UTF-8 -*-
"""
归并排序。
核心思想也是分治法，先递归分解数组，然后再合并数组
"""


def merge_sort(alist):
    if not alist or len(alist) < 2:
        return alist
    n = len(alist)
    mid = int(n / 2)
    # left_li是对原列表左半部分进行归并排序后，返回的有序新列表
    left_li = merge_sort(alist[:mid])
    # right_li是对原列表右半部分进行归并排序后，返回的有序新列表
    right_li = merge_sort(alist[mid:])
    # 最后将这两个有序的子序列合并为一个新列表，并返回
    return merge(left_li, right_li)


def merge(left_li, right_li):
    res = []
    left, right = 0, 0
    while left < len(left_li) and right < len(right_li):
        # 稳定性排序
        if left_li[left] <= right_li[right]:
            res.append(left_li[left])
            left += 1
        else:
            res.append(right_li[right])
            right += 1
    res.extend(left_li[left:])
    res.extend(right_li[right:])
    return res


if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("归并排序前：", alist)
    # 这里与之前的排序不一样，这里是返回一个排好序的新列表，原列表没有改变
    res = merge_sort(alist)
    print("归并排序后：", res)
