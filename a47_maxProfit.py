# -*- coding: UTF-8 -*-
"""
买卖股票的最佳时机。
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
注意：你不能在买入股票前卖出股票。

示例 1:
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

示例 2:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

解题思路：
方法一：双重for循环，暴力破解。Python3运行超时
方法二：一次遍历。贪心算法
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        res = 0
        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res


class Solution2:
    # 方法二：一次遍历。贪心算法
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(price - min_price, max_profit)
            min_price = min(price, min_price)
        return max_profit


if __name__ == '__main__':
    li = [7, 1, 5, 3, 6, 4]
    s = Solution2()
    print(s.maxProfit(li))
