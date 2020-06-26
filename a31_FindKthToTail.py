#-*- coding: UTF-8 -*-

"""
链表中倒数第k个结点。
输入一个链表，输出该链表中倒数第k个结点。
借助两个临时指针变量p1、p2，p1先走到第k个位置
"""

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

def FindKthToTail(pHead,k):
    if not pHead or k<1:
        return None
    p1 = pHead
    p2 = None
    # p1从第一个位置(pHead)向后移动k-1个位置，到达第k个位置
    for _ in range(k-1):
        if p1.next:
            p1 = p1.next
        else:
            # 链表长度不足k
            return None
    # 原本是p1从第k个位置移动到None，与此同时，p2从None移动到倒数第k个位置。即 p1为None时，p2移动到了倒数第k个位置
    # 但为了确保p2.next可执行，先将p2移动到pHead，则此时p1需要少移动一步。即 p1.next为None时，p2移动到了倒数第k个位置
    p2 = pHead
    while p1.next:
        p1 = p1.next
        p2 = p2.next
    return p2