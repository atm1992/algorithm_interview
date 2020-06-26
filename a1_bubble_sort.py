# -*- coding: UTF-8 -*-
"""
冒泡排序。
小的元素会通过交换位置的方式像冒泡一样慢慢浮到数列的头部
第 i 次排序是对当前数列中的前 n-i+1 个元素进行排序，从这 n-i+1 个元素中的第一个元素开始，比较相邻的两个元素，若前一个大于后一个，则交换这两个元素的位置
"""


def bubble_sort(alist):
    if not alist or len(alist) < 2:
        return
    n = len(alist)
    # 待排序数列的最后一个元素下标从 n-1 一直到 1
    for i in range(n - 1, 0, -1):
        change_count = 0
        for j in range(i):
            # 稳定性排序
            if alist[j] > alist[j + 1]:
                change_count += 1
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
        # 若此次排序没有交换元素位置，则排序终止
        if change_count == 0:
            break


if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("冒泡排序前：", alist)
    bubble_sort(alist)
    print("冒泡排序后：", alist)
