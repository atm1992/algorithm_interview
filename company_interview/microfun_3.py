# -*- coding: UTF-8 -*-

class Solution:
    def maxWidth(self, A):
        res = 0
        while A:
            if len(A) <= res:
                break
            front, rear = 0, len(A) - 1
            while front < rear:
                if A[front] <= A[rear]:
                    if (rear - front) > res:
                        res = rear - front
                    break
                rear -= 1
            A = A[1:]
        return res
