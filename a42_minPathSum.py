# -*- coding: UTF-8 -*-
"""
最小路径和。
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

解题思路：
方法一：使用递归进行暴力破解。
对于每个元素，可以考虑两条路径：向右走或向下走，在这两条路径中选择路径权值和较小的那个。
cost(i,j)=grid[i][j]+min(cost(i+1,j),cost(i,j+1))
时间复杂度：O(2^(m+n))
空间复杂度：O(m+n)

方法二：二维动态规划。
新建一个与原矩阵大小相同的二维数组dp，从右下角开始填写dp数组，
dp数组中的每个元素值为原矩阵中该位置到右下角的最小路径和，最后返回dp[0][0]
时间复杂度：O(mn)
空间复杂度：O(mn)

方法三：二维动态规划（直接在原矩阵中修改，不需要使用额外存储空间）。
走到当前单元格(i,j)的最小路径和 = “从左方单元格(i-1,j)与从上方单元格(i,j−1)走来的两个最小路径和中较小的 ” + 当前单元格的值grid[i][j]。
既可以是从左上角走到右下角，也可以是从右下角走到左上角。只是最终返回结果在二维数组中的位置不同而已
时间复杂度：O(mn)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    # 方法一：使用递归进行暴力破解。Python3运行超时
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 获取从(i,j)到(rows-1,cols-1)的最小路径和
        def cost(grid: List[List[int]], i: int, j: int):
            rows = len(grid)
            cols = len(grid[0])
            if i >= rows or j >= cols:
                return float('inf')
            if i == rows - 1 and j == cols - 1:
                return grid[i][j]
            return grid[i][j] + min(cost(grid, i + 1, j), cost(grid, i, j + 1))

        return cost(grid, 0, 0)


class Solution2:
    # 方法二：二维动态规划。从右下角走到左上角，最终返回左上角位置的值
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        # 从最后一行开始填写dp数组
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if i == rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j]
                elif i == rows - 1 and j < cols - 1:
                    dp[i][j] = grid[i][j] + dp[i][j + 1]
                elif i < rows - 1 and j == cols - 1:
                    dp[i][j] = grid[i][j] + dp[i + 1][j]
                else:
                    dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]


class Solution3:
    # 方法三：二维动态规划（直接在原矩阵中修改，不需要使用额外存储空间）。从左上角走到右下角，最终返回右下角位置的值
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


if __name__ == '__main__':
    li = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    s = Solution3()
    print(s.minPathSum(li))
