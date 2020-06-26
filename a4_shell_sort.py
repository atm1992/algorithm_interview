# -*- coding: UTF-8 -*-
"""
希尔排序，也叫缩小增量(gap)排序。
对于第 i 次排序，增量gap = n/(2的 i 次方)（向下取整），元素下标 i 从gap逐步增长到 n-1，由下标为 i、i-gap、i- 2*gap … 的元素组成一个子序列，对这个子序列执行插入排序
"""


def shell_sort(alist):
    if not alist or len(alist) < 2:
        return
    n = len(alist)
    gap = int(n / 2)
    # 最后一次排序为gap等于1，gap小于1时终止排序
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                # 不稳定排序。如：[5, 3, 3, 2]
                if alist[j - gap] > alist[j]:
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                else:
                    # 减少不必要的比较次数
                    break
        gap = int(gap / 2)


if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("希尔排序前：", alist)
    shell_sort(alist)
    print("希尔排序后：", alist)
