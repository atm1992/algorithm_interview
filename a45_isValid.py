#-*- coding: UTF-8 -*-
"""
有效的括号。
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
1、左括号必须用相同类型的右括号闭合。
2、左括号必须以正确的顺序闭合。
3、注意空字符串可被认为是有效字符串。

解题思路：
"""


class Solution:
    # 注意：给定字符串只包含上述3类括号，没有其它字符
    # 空字符串需要返回True
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in dic:
                # 若当前栈为空 或 前一个字符不是匹配的左括号，则直接返回False
                # 这里使用到了or的短路运算，若前一个条件为True，则后一个条件不执行
                if not stack or dic[i] != stack.pop():
                    return False
            else:
                # 因为给定字符串只包含上述3类括号，所以这里append的都是左括号，匹配到右括号时，就出栈
                stack.append(i)
        # 最终若栈为空，则返回True
        return not stack
