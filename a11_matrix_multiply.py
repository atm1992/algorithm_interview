# -*- coding: UTF-8 -*-
"""
二维矩阵相乘。
"""


def matrix_multiply(A, B):
    row_len = len(A)
    col_len = len(B[0])
    cross_len = len(A[0])
    # 结果矩阵初始化。不能写成 [[0] * col_len] * row_len
    # 将一个list乘以k，表面上是将list复制了k份，事实上这k个list所指向的对象只有一个，即 原始的list，
    # 也就是说 改变任何一个list，其余 k-1 个list的值也会跟着改变
    res = [[0] * col_len for _ in range(row_len)]
    for i in range(row_len):
        for j in range(col_len):
            for k in range(cross_len):
                res[i][j] += A[i][k] * B[k][j]
    return res


if __name__ == '__main__':
    A = [[1, 1, 1], [2, 0, 2]]
    B = [[0, 1], [1, 0], [1, 1]]
    print(matrix_multiply(A, B))
