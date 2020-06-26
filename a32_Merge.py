#-*- coding: UTF-8 -*-

"""
合并两个排序的链表。
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

解题思路：使用递归或者循环
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def Merge(pHead1,pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    if pHead1.val <= pHead2.val:
        pMergeHead = pHead1
        pMergeHead.next = Merge(pHead1.next,pHead2)
    else:
        pMergeHead = pHead2
        pMergeHead.next = Merge(pHead1,pHead2.next)
    return pMergeHead
