"""
1. linux上的文件a.txt 
\n字段分隔，\t换行
求第二列中含有'yuanfudao'的行数？

考点：awk命令
"""

"""
2. 二叉树，求从根节点到叶子节点的路径上的节点值的和的最大值

                    4
         3                         8
9                  1         2              1
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        


def construct_tree(nums, i):
    
    if i >= len(nums):
        return None
    
    node = Node(nums[i])
    node.left = construct_tree(nums, 2*i+1)
    node.right = construct_tree(nums, 2*i+2)
    
    return node
    
def bfs(root):
    
    if root.left == None and root.right == None:
        return root.val
    else:
        
        a = root.val + bfs(root.left)
        b = root.val + bfs(root.right)
        return max(a, b)        
        
nums = [4, 3, 8, 9, 1, 2, 1]    
root = construct_tree(nums, 0)   
ret = bfs(root)
