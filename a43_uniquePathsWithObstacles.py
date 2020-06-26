# -*- coding: UTF-8 -*-
"""
不同路径 II。
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
说明：m 和 n 的值均不超过 100。

示例 1:
输入:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
输出: 2
解释:
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

解题思路：
二维动态规划（直接在原矩阵中修改，不需要使用额外存储空间）。
对于起点(0,0)位置，若该位置上有障碍物，则直接返回0，表示没有路径可以到达右下角。否则赋值为1
对于第一行的所有位置，只能是从(0,0)向右一步步走过来的，若其中某个位置存在障碍物，则该位置及其右方的所有位置均赋值为0，
表示从(0,0)到达这些位置的路径数为0；否则赋值为1，表示从(0,0)到达这些位置的路径数为1。
对于第一列的所有位置，只能是从(0,0)向下一步步走过来的，若其中某个位置存在障碍物，则该位置及其下方的所有位置均赋值为0，
表示从(0,0)到达这些位置的路径数为0；否则赋值为1，表示从(0,0)到达这些位置的路径数为1。
对于其余位置，若该位置上有障碍物，则该位置的值赋为0；否则赋值为左边位置的值 + 上边位置的值，
表示从左边走过来的路径数加上从上边走过来的路径数。
最终返回右下角位置的值。
时间复杂度：O(mn)
空间复杂度：O(1)
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        for i in range(1, rows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        for j in range(1, cols):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)
        for i in range(1, rows):
            for j in range(1, cols):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return obstacleGrid[-1][-1]
