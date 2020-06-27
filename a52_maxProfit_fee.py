# -*- coding: UTF-8 -*-
"""
买卖股票的最佳时机含手续费。
给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易是指买入持有并卖出股票的整个过程，每笔交易你只需支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

注意:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.

解题思路：动态规划
由于这里是不限交易次数，因此交易次数K这个维度对利润没有影响。dp数组由三维变为二维。
另外，由于存在手续费，因此，需要修改状态转移方程：
dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
解释：今天没有持有股票，有两种可能：
1、昨天就没有持有，今天选择不变，所以今天还是没有持有；
2、昨天持有股票，但是今天卖出，所以今天没有持有股票了。卖出股票需要手续费

dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
解释：今天持有股票，有两种可能：
1、昨天持有股票，今天选择不变，所以今天还持有股票；
2、昨天没有持有，今天选择买入，所以今天持有了股票。

初始值依旧为：
dp[0][0] = 0
dp[0][1] = -prices[0]
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


class Solution2:
    # 空间复杂度降为O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        dp_i0 = 0
        dp_i1 = -prices[0]
        for i in range(1, n):
            tmp = dp_i0
            dp_i0 = max(dp_i0, dp_i1 + prices[i] - fee)
            dp_i1 = max(dp_i1, tmp - prices[i])
        return dp_i0
