'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
假设数组中不存在重复的元素
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
'''

def search(nums, s, e, target):
    if s > e:
        return -1
        
    mid = (s + e) / 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] > nums[s]:  # 前半段有序
        if nums[s] <= target < nums[mid]:
            search(nums, s, mid-1, target)
        else:
            search(nums, mid+1, e, target)
    else:
        if nums[mid] < target <= nums[e]:
            search(nums, mid+1, e, target)
        else:
            search(nums, s, mid-1, target)
    
'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

https://leetcode-cn.com/problems/validate-binary-search-tree/


'''



'''
spark 分区器
spark shuffle
map与mapPartition区别
spark的作业提交流程
宽依赖、窄依赖
hive外部表内部表区别
'''




