# -*- coding: UTF-8 -*-
"""
接雨水。
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
例如：输入数组 [0,1,0,2,1,0,1,3,2,1,2,1]，输出 6

解题思路：
双指针法
使用left,right两个指针逐步向中间移动，使用maxleft、maxright这两个变量来存储当前的左右两侧最大值
若maxleft小于maxright，则left移动一步；否则right移动一步，直到left小于right
时间复杂度O(N)，空间复杂度为O(1)
"""
from typing import List


class Solution:
    """双指针法"""

    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        n = len(height)
        maxleft, maxright = height[0], height[n - 1]
        left, right = 1, n - 2
        res = 0
        while left <= right:
            # 更新maxleft, maxright
            # 确保此时的maxleft一定大于等于height[left]，从而确保maxleft-height[left]大于等于0
            maxleft = max(height[left], maxleft)
            maxright = max(height[right], maxright)
            # 能否盛水，盛多少水，取决于短板（矮的那个）
            if maxleft < maxright:
                # res每次累加的都是当前柱子上能接多少雨水，所以当left = right时，累加的是left和right最后共同指向的那根柱子
                res += maxleft - height[left]
                left += 1
            else:
                res += maxright - height[right]
                right -= 1
        return res
