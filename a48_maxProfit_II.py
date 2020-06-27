# -*- coding: UTF-8 -*-
"""
买卖股票的最佳时机 II。
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 
提示：
1 <= prices.length <= 3 * 10 ^ 4
0 <= prices[i] <= 10 ^ 4

解题思路：
方法一：暴力破解法。Python3运行超时
时间复杂度：O(n^n)，调用递归函数 n^n 次。
空间复杂度：O(n)，递归的深度为 n 。

方法二：峰谷法
以 [7, 1, 5, 3, 6, 4] 为例，(6-1) < (5-1) + (6-3) = (6-1) + (5-3)
从第一个波谷开始向后查找最近的波峰，得到一次利润；然后向后查找最近的波谷，再向后查找最近的波峰，再得到一次利润 ……
这比第二次的波峰减去第一次的波谷，所得到的利润要高。因为是第二次的波谷是紧邻着第一次波峰后面的，所以可以确保第二次的波谷一定小于第一次的波峰
时间复杂度：O(n)
空间复杂度：O(1)

方法三：一次遍历。贪心算法
不需要考虑波峰、波谷，只要后一个值大于前一个值，就把它们的差值加到利润中
时间复杂度：O(n)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def calculate(prices: List[int], start: int) -> int:
            n = len(prices)
            # 递归终止条件
            if start >= n:
                return 0
            max_profit_final = 0
            for i in range(start, n - 1):
                max_profit_cur = 0
                for j in range(i + 1, n):
                    if prices[j] > prices[i]:
                        profit = prices[j] - prices[i] + calculate(prices, j + 1)
                        max_profit_cur = max(profit, max_profit_cur)
                max_profit_final = max(max_profit_cur, max_profit_final)
            return max_profit_final

        return calculate(prices, 0)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        start = 0
        n = len(prices)
        valley_cur, peak_cur = prices[0], prices[0]
        res = 0
        while start < n - 1:
            # 找到波谷时退出循环，prices[start] < prices[start+1]
            while start < n - 1 and prices[start] >= prices[start + 1]:
                start += 1
            valley_cur = prices[start]
            # 找到波峰时退出循环，prices[start] > prices[start+1]
            while start < n - 1 and prices[start] <= prices[start + 1]:
                start += 1
            peak_cur = prices[start]
            res += peak_cur - valley_cur
        return res


class Solution3:
    # 方法三：一次遍历。贪心算法
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                res += prices[i] - prices[i - 1]
        return res


if __name__ == '__main__':
    s = Solution()
    li = [7, 6, 4, 3, 1]
    print(s.maxProfit(li))
