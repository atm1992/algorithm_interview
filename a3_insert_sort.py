#-*- coding: UTF-8 -*-
"""
插入排序。
第 i 次排序是将第 i+1 个元素插入到前面长度为 i、已经按值有序的子序列中，从后往前扫描已排好序的子序列，找到相应位置然后插入
"""

def insert_sort(alist):
    if not alist or len(alist)<2:
        return
    n = len(alist)
    for i in range(1,n):
        for j in range(i,0,-1):
            # 稳定性排序
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
            else:
                # 减少不必要的比较次数
                break

if __name__ == '__main__':
    alist = [2, 1, 45, 1, 21, 4, 2, 6, 9]
    print("插入排序前：", alist)
    insert_sort(alist)
    print("插入排序后：", alist)