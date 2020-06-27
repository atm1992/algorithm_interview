# -*- coding: UTF-8 -*-
"""
买卖股票的最佳时机 IV。
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [2,4,1], k = 2
输出: 2
解释: 在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2:
输入: [3,2,6,5,0,3], k = 2
输出: 7
解释: 在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

解题思路：动态规划
每天的最大利润受3个维度影响：
1、今天是第几天，0 <= i < n。每天的股票价格不一样
2、今天是第几次交易，1 <= k <= K。买入股票时，交易次数加1。当然也可选择在卖出股票时，交易次数加1
3、今天是否持有股票，1 持有，0 未持有。卖出股票时，利润增加；买入股票时，利润减少

状态转移方程：
dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
解释：今天没有持有股票，有两种可能：
1、昨天就没有持有，今天选择不变，所以今天还是没有持有；
2、昨天持有股票，但是今天卖出，所以今天没有持有股票了。

dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
解释：今天持有股票，有两种可能：
1、昨天持有股票，今天选择不变，所以今天还持有股票；
2、昨天没有持有，今天选择买入，所以今天持有了股票。

初始值：
dp[i][0][0] = 0
解释：k为0，表示没有进行过交易。因此无论i为多少，利润都为0
dp[i][0][1] = float('-inf')
解释：k为0，表示没有进行过交易，因此不可能会持有股票
dp[0][k][0] = 0
解释：无论k为大于0的任何数，只要当前没有持股，利润就一直为0
dp[0][k][1] = -prices[0]
解释：无论k为大于0的任何数，利润都是 -prices[0]
"""
from typing import List


class Solution:
    # 运行超时。内存溢出，因为三维数组dp太大
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) < 2 or k < 1:
            return 0
        n = len(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        # return dp[n - 1][k][0]
        return dp[-1][-1][0]


class Solution2:
    """
    有效的交易由买入和卖出构成，至少需要两天；反之，当天买入当天卖出则视为一次无效交易。若给定的最大交易次数 k <= n/2，
    则这个 k 可以有效约束交易次数；若给定的 k > n/2 ，则这个 k 实际上起不到约束作用，此时的k等价于正无穷，问题退化为不限交易次数。
    """

    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices or len(prices) < 2 or k < 1:
            return 0

        def maxProfit_k_inf(prices):
            n = len(prices)
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    res += prices[i] - prices[i - 1]
            return res

        def maxProfit_k_others(prices, k):
            n = len(prices)
            dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
            for i in range(n):
                for j in range(1, k + 1):
                    if i == 0:
                        dp[i][j][0] = 0
                        dp[i][j][1] = -prices[0]
                    else:
                        dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                        dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
            # return dp[n - 1][k][0]
            return dp[-1][-1][0]

        n = len(prices)
        if k > n / 2:
            return maxProfit_k_inf(prices)
        else:
            return maxProfit_k_others(prices, k)
