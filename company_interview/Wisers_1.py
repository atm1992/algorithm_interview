# -*- coding: UTF-8 -*-
"""
给定一个无序正整数数组，要求抽去其中两个元素，使得数组分为3段，这3段子数组的累加和相等。
若能找到这样的分段，则返回一个二维数组，其中包含3个子数组。若无法找到，则返回空数组
例如：对于[4, 2, 3, 1, 5, 8, 6]，抽去元素3、8，返回 [[4, 2], [1, 5], [6]]
"""


def func(li):
    res = []
    left, right = 0, len(li) - 1
    left_sum, right_sum = li[left], li[right]
    while right - left >= 4:
        if left_sum == right_sum:
            mid_sum = sum(li[left + 2:right - 1])
            if left_sum == mid_sum:
                res.append(li[:left + 1])
                res.append(li[left + 2:right - 1])
                res.append(li[right:])
                break
            elif left_sum < mid_sum:
                left += 1
                left_sum += li[left]
            else:
                break
        elif left_sum < right_sum:
            left += 1
            left_sum += li[left]
        else:
            right -= 1
            right_sum += li[right]
    return res


if __name__ == '__main__':
    li = [4, 2, 3, 1, 5, 8, 6]
    print(func(li))
