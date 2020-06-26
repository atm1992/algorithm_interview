# -*- coding: UTF-8 -*-

class Solution:
    def minDeletionSize(self, A):
        if not A or len(A) < 2:
            return 0
        res = 0
        n = len(A)
        m = len(A[0])
        for i in range(m):
            count = 0
            for j in range(1, n):
                if A[j][i] < A[j - 1][i]:
                    res += 1
                    break
                else:
                    count += 1
            if count == n - 1:
                break
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.minDeletionSize(["xc", "yb", "za"]))
