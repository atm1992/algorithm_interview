# -*- coding: UTF-8 -*-
"""
最长回文子串。
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2：
输入: "cbbd"
输出: "bb"

解题思路：
方法一：中心扩散法
从左向右遍历给定字符串，以当前字符为中心，向左右两侧扩散
1、首先，判断左右两侧的字符与当前字符是否相同，若相同，则以这奇数个或偶数个相同字符组成的子串作为中心
2、然后，左右两侧同时遍历，判断left指向的字符与right指向的字符是否相同，若相同，则继续遍历；若不同，则停止遍历
3、以下一个字符为中心，重复上述过程
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """方法一：中心扩散法"""
        if not s or len(s) < 2:
            return s
        n = len(s)
        max_len = 1
        max_start = 0
        for i in range(n):
            cur_len = 1
            left = i - 1
            right = i + 1
            while left >= 0 and s[left] == s[i]:
                left -= 1
                cur_len += 1
            while right < n and s[right] == s[i]:
                right += 1
                cur_len += 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                cur_len += 2
            if cur_len > max_len:
                max_len = cur_len
                max_start = left + 1
        return s[max_start:max_start + max_len]
