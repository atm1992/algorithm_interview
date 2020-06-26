# -*- coding: UTF-8 -*-

"""
用两个栈实现队列。
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

解题思路：
栈 —— 后进先出。栈的push、pop操作都是在栈顶（可看作是队尾）
队列 —— 先进先出。队列的push操作在队尾，pop操作在队头
"""


class Solution:
    def __init__(self):
        # stack1的push实现队列的push
        self.stack1 = []
        # 先从尾部pop出stack1的元素，然后push到stack2的尾部。
        # 注意：需要pop完stack1中的所有元素，此时stack2的尾部元素就是原来的队头元素
        # 因此，stack2的pop便可实现队列的pop
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        # 若stack2中还有元素，则直接先pop掉其中的元素
        if self.stack2:
            return self.stack2.pop()
        # 若stack2中没有元素，而stack1中还有元素，则将stack1中的所有元素都转移到stack2中
        elif self.stack1:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        # stack1和stack2中都没有元素
        else:
            return None
