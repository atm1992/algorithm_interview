# -*- coding: UTF-8 -*-
"""
二分查找。
"""


# 基础版本
def binarySerach(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# 查找第一个等于key的元素
def binarySerach_1(arr, target):
    left, right = 0, len(arr) - 1
    # 退出循环时，left>right
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    if left < len(arr) and arr[left] == target:
        return left
    else:
        return -1


# 查找最后一个等于key的元素
def binarySerach_2(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            right = mid + 1
        else:
            left = mid - 1
    if right >= 0 and arr[right] == target:
        return right
    else:
        return -1


# 查找最后一个等于或小于key的元素
def binSearch_3(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return right


# 查找最后一个小于key的元素
def binSearch_4(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return right


# 查找第一个等于或大于key的元素
def binSearch_5(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left


# 查找第一个大于key的元素
def binSearch_6(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
