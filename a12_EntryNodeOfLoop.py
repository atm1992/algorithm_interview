# -*- coding: UTF-8 -*-
"""
链表中环的入口结点。
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

解题思路：使用双指针fast、slow，两个指针同时从头结点出发，fast每次移动两个结点，slow每次移动一个结点。
若存在环，这两个指针必定在环上某结点处相遇，相遇时，slow走了x步，fast走了2x步，令头结点到环入口结点为a步，slow在环中走了b步，环的长度为n，则：
x = a+b; 2x = x+kn（k为大于等于1的整数，表示fast比slow在环上多走了k圈）
可得，a+b = kn; a = kn-b
因为slow已经在环上走了b步，所以再走kn-b（即 a）步，slow将会达到环的入口结点处
此时将fast改为每次移动一个结点从头结点走向环入口结点，需要a步便可以走到环的入口结点处
即 fast从头结点开始走，slow从相遇点开始走，各走a步，便都会走到环的入口结点处，此时fast与slow相遇。这个过程中，并不需要统计具体走了多少步，
只需判断fast与slow是否相遇即可，相遇时肯定就在环的入口结点处
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def EntryNodeOfLoop(pHead):
    # 若链表中存在环，则永远不会有None节点。若存在None节点，说明不存在环
    if not pHead or not pHead.next:
        return None
    fast, slow = pHead, pHead
    fast = fast.next.next
    slow = slow.next
    # 当fast与slow在环中某点相遇时，退出循环
    while fast != slow:
        if not fast or not fast.next:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = pHead
    # fast 与 slow 相遇在入口点时，退出循环
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast
