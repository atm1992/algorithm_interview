# -*- coding: UTF-8 -*-
"""
堆排序。不稳定排序
将原始待排序数列中的n个元素构造为初始堆（最大堆、大顶堆），其中的最大值位于第一个位置，将第一个位置的元素（最大值）与最后一个位置的元素（不一定最小）进行交换
升序排序使用最大堆；降序排序使用最小堆
初始化堆：从最后一个非叶子节点开始往前构造
更新堆：只需调整根节点的位置
"""


def heap_sort(alist):
    if not alist or len(alist) < 2:
        return
    heap_size = len(alist)
    max_heap(alist, heap_size)      # 初始化
    while heap_size > 1:            # 堆内元素多于1个
        # 交换堆顶元素和最后一个元素
        alist[0], alist[heap_size - 1] = alist[heap_size - 1], alist[0]
        heap_size -= 1
        max_heap(alist, heap_size)  # 更新堆


# 大顶堆，升序
def max_heap(alist, heap_size):
    if heap_size < 2:
        return
    end = int(heap_size / 2) - 1    # 最后一个非叶子节点的下标
    # 初始化，从最后一个非叶子节点开始调整；更新堆，只需从根节点开始调整
    # 若heap_size 等于 len(alist)，则说明初始化
    start = end if heap_size == len(alist) else 0
    # start 的取值范围为：[0, end]
    while start >= 0:
        i = start
        while i <= end:
            l = 2 * i + 1  # 左孩子的下标
            r = 2 * i + 2  # 右孩子的下标
            max_idx = r if r < heap_size and alist[r] >= alist[l] else l
            if alist[i] >= alist[max_idx]:
                break
            else:
                alist[i], alist[max_idx] = alist[max_idx], alist[i]
                i = max_idx
        start -= 1


# 小顶堆，降序
def min_heap(alist, heap_size):
    if heap_size < 2:
        return
    end = int(heap_size / 2) - 1    # 最后一个非叶子节点的下标
    # 初始化，从最后一个非叶子节点开始调整；更新堆，只需从根节点开始调整
    # 若heap_size 等于 len(alist)，则说明初始化
    start = end if heap_size == len(alist) else 0
    # start 的取值范围为：[0, end]
    while start >= 0:
        i = start
        while i <= end:
            l = 2 * i + 1  # 左孩子的下标
            r = 2 * i + 2  # 右孩子的下标
            min_idx = r if r < heap_size and alist[r] <= alist[l] else l
            if alist[i] <= alist[min_idx]:
                break
            else:
                alist[i], alist[min_idx] = alist[min_idx], alist[i]
                i = min_idx
        start -= 1


if __name__ == '__main__':
    alist = [7, 95, 73, 65, 60, 77, 28, 62, 43]
    print("堆排序前：", alist)
    heap_sort(alist)
    print("堆排序后：", alist)
