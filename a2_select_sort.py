# -*- coding: UTF-8 -*-

"""
选择排序。
第 i 次排序是对当前数列中的后 n-i+1 个元素进行排序，从这 n-i+1 个元素中从前往后选出最小的元素，然后将该元素与这 n-i+1 个元素中的第一个元素交换位置
"""


def select_sort(alist):
    if not alist or len(alist) < 2:
        return
    n = len(alist)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            # 这里无论使用< 还是 <=，都是不稳定排序
            # 使用< ，反例 [3,5,3,2]
            # 使用<= ，反例 [3,5,3]
            if alist[j] < alist[min_idx]:
                min_idx = j
        if min_idx != i:
            alist[min_idx], alist[i] = alist[i], alist[min_idx]


if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("选择排序前：", alist)
    select_sort(alist)
    print("选择排序后：", alist)
