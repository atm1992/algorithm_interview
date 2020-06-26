#-*- coding: UTF-8 -*-

"""
反转链表。
输入一个链表，反转链表后，输出新链表的表头。

解题思路：使用递归或者循环
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    pReverseHead = None
    pPrev,pNode = None,pHead
    while pNode:
        pNext = pNode.next
        # 只有当pNext为None时，才给pReverseHead赋值为pNode
        if not pNext:
            pReverseHead = pNode
        pNode.next = pPrev
        pPrev = pNode
        pNode = pNext
    return pReverseHead