# -*- coding: UTF-8 -*-
"""
买卖股票的最佳时机 III。
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:
输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。

示例 2:
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。  
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。  
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

示例 3:
输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
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

方法二：从状态转移方程中可发现，计算当前状态只需使用到dp[i - 1][k][0]、dp[i - 1][k][1]、dp[i - 1][k - 1][0]，所以可以考虑
使用3个变量来存储这些值，从而降低空间复杂度
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_k = 2
        # 定义一个三维数组dp
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        # 初始化
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for k in range(1, max_k + 1):
            dp[0][k][0] = 0
            dp[0][k][1] = -prices[0]
        for i in range(1, n):
            for k in range(1, max_k + 1):
                # 昨天就没有股票；或者昨天有股票，今天卖出
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                # 昨天就有股票；或者昨天没有股票，今天买入，买入股票后，k会加1
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 最后一天，有2次交易，并且没有持股。此时的利润为最终利润
        # return dp[n - 1][2][0]
        return dp[-1][-1][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        n = len(prices)
        max_k = 2
        # 定义一个三维数组dp
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(1, max_k + 1):
                # 定义第一天的状态
                if i == 0:
                    # 无论k为多少，只要当前没有持股，利润就一直为0。未进行过交易 or 买入、卖出 or 买入、卖出、买入、卖出 ……
                    dp[i][k][0] = 0
                    # 无论k为大于0的任何数，利润都是 -prices[0]。买入 or 买入、卖出、买入 ……
                    # 若k为0，则表示没有进行过交易，因此不可能会持有股票，此时的值为float('-inf')
                    dp[i][k][1] = -prices[0]
                else:
                    """
                    下面的状态转移方程，只有dp[i - 1][k - 1][0]会使用到dp[x][0][0]，对于任意一天的dp[x][0][0]，值都是0。
                    因为三维数组dp的初始值原本就为0，所以无需再赋值。
                    对于任意一天的dp[x][0][1]，值都是float('-inf')，但是状态转移方程中并没有使用到该值，所以也无需再赋值。
                    """
                    # 昨天就没有股票；或者昨天有股票，今天卖出
                    dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                    # 昨天就有股票；或者昨天没有股票，今天买入，买入股票后，k会加1
                    dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 最后一天，有2次交易，并且没有持股。此时的利润为最终利润
        # return dp[n - 1][2][0]
        return dp[-1][-1][0]


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        # 定义第一天的状态
        dp_i10 = 0
        dp_i20 = 0
        dp_i11 = -prices[0]
        dp_i21 = -prices[0]
        for price in prices[1:]:
            dp_i10 = max(dp_i10, dp_i11 + price)
            # 因为对于任意一天的dp[x][0][0]，值都是0
            dp_i11 = max(dp_i11, -price)
            dp_i20 = max(dp_i20, dp_i21 + price)
            dp_i21 = max(dp_i21, dp_i10 - price)
        # 最后一天，有2次交易，并且没有持股。此时的利润为最终利润
        return dp_i20


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5]
    s = Solution2()
    print(s.maxProfit(li))
