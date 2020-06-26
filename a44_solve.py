# -*- coding: UTF-8 -*-
"""
被围绕的区域。
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。
找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
示例:
X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：
X X X X
X X X X
X X X X
X O X X
解释:
被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

解题思路：
转换思路，找到所有被 'X' 围绕的区域不容易，但可将问题转化为找到边界上所有的'O'以及与这些'O'相连的 'O'，将这些'O'先替换为'#'，
然后遍历二维矩阵中的所有位置，将所有的'O'替换为'X'，将所有的'#'替换回'O'
方法一：DFS
方法二：BFS
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows, cols = len(board), len(board[0])
        # 若所有位置都在边界，则无需进行任何替换
        if rows < 3 or cols < 3:
            return

        def dfs(i, j):
            board[i][j] = '#'
            # 递归搜索当前位置的上下左右四个位置
            for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < rows and 1 <= tmp_j < cols and board[tmp_i][tmp_j] == 'O':
                    dfs(tmp_i, tmp_j)

        for i in range(rows):
            # 第一列
            if board[i][0] == 'O':
                dfs(i, 0)
            # 最后一列
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)

        for j in range(cols):
            # 第一行
            if board[0][j] == 'O':
                dfs(0, j)
            # 最后一行
            if board[rows - 1][j] == 'O':
                dfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        rows, cols = len(board), len(board[0])
        # 若所有位置都在边界，则无需进行任何替换
        if rows < 3 or cols < 3:
            return

        def bfs(i, j):
            queue = [(i, j)]
            while queue:
                m, n = queue.pop(0)
                if 0 <= m < rows and 0 <= n < cols and board[m][n] == 'O':
                    board[m][n] = '#'
                    for (x, y) in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        queue.append((m + x, n + y))

        for i in range(rows):
            # 第一列
            if board[i][0] == 'O':
                bfs(i, 0)
            # 最后一列
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)

        for j in range(cols):
            # 第一行
            if board[0][j] == 'O':
                bfs(0, j)
            # 最后一行
            if board[rows - 1][j] == 'O':
                bfs(rows - 1, j)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
