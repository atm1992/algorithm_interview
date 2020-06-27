# -*- coding: UTF-8 -*-
"""
最佳买卖股票时机含冷冻期。
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

示例:
输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

解题思路：动态规划
由于这里是不限交易次数，因此交易次数K这个维度对利润没有影响。dp数组由三维变为二维。
另外，由于存在冷冻期1天，若选择在第i天买入股票，则状态需要从第 i-2 天转移

因此，状态转移方程为：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
解释：今天没有持有股票，有两种可能：
1、昨天就没有持有，今天选择不变，所以今天还是没有持有；
2、昨天持有股票，但是今天卖出，所以今天没有持有股票了。

dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
解释：今天持有股票，有两种可能：
1、昨天持有股票，今天选择不变，所以今天还持有股票；
2、前天没有持有，今天选择买入，所以今天持有了股票。

由于状态转移方程中出现了dp[i-2] 以及 dp[i-1]，所以初始值需要考虑第一天和第二天的状态：
dp[0][0] = 0
dp[0][1] = -prices[0]
dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
dp[1][1] = max(dp[0][1], dp[-1][0] - prices[1]) = max(dp[0][1], -prices[1])
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        # 定义一个二维数组dp
        dp = [[0] * 2 for _ in range(n)]
        # 初始化
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[1][0] = max(dp[0][0], dp[0][1] + prices[1])
        dp[1][1] = max(dp[0][1], -prices[1])
        for i in range(2, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[-1][0]


class Solution2:
    # 空间复杂度降为O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        # 初始化
        dp_i0 = 0
        dp_i1 = -prices[0]
        dp_pre0 = 0  # 表示dp[i - 2][0]的初始值，即 dp[-1][0]
        for i in range(1, n):
            tmp = dp_i0
            dp_i0 = max(dp_i0, dp_i1 + prices[i])
            dp_i1 = max(dp_i1, dp_pre0 - prices[i])
            dp_pre0 = tmp
        return dp_i0
