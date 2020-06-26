# -*- coding: UTF-8 -*-

"""
字符串的排列。
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

解题思路：
首先，将输入的字符串转换为字符数组
然后，固定排列中的第一个字符，通过递归求出后面其它所有字符组成的排列，然后在前面拼接上第一个字符
接着，通过循环来更换上述的第一个字符
最后，对重复字符的处理：将字符数组进行排序，相同的字符将会处于相邻位置，重复字符只需处理其中一个即可，剩余的重复字符跳过
"""


def Permutation(ss):
    if not ss:
        return []
    n = len(ss)
    sl = list(ss)
    if n == 1:
        return sl
    # 按字典序排序
    sl.sort()
    res = []
    for i in range(n):
        # 处理重复字符
        if i > 0 and sl[i] == sl[i - 1]:
            continue
        # 将当前字符以外的其余所有字符通过递归求解
        temp = Permutation("".join(sl[:i]) + "".join(sl[i + 1:]))
        for t in temp:
            res.append(sl[i] + t)
    return res


if __name__ == '__main__':
    print(Permutation("abc"))
