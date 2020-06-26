# -*- coding: UTF-8 -*-

"""
栈的压入、弹出序列。
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

解题思路：使用一个栈来模拟压入弹出操作

可以使用Python数组来实现栈，Python数组的append、pop操作都是在数组的末尾进行，因此可把数组的末尾当做栈顶。
注意：执行pop操作时，数组不能为空
"""


def IsPopOrder(pushV, popV):
    if not pushV or not popV or len(pushV) != len(popV):
        return False
    stack = []
    for i in pushV:
        stack.append(i)
        while len(stack) > 0 and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
    if len(stack) > 0:
        return False
    else:
        return True
