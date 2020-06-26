# -*- coding: UTF-8 -*-

"""
二叉树的后序遍历。
先使用递归后序遍历左子树上的所有节点，然后使用递归后序遍历右子树上的所有节点，最后访问根节点

深度优先遍历 使用递归或栈
广度优先遍历 使用队列
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def pre_in_build_tree(pre, tin):
    """使用前序序列和中序序列构建二叉树。要求所输入的前序序列和中序序列中不含重复数字，
            因为需要根据数值来确定根节点在中序序列中的位置"""
    if not pre or not tin or len(pre) != len(tin):
        return None
    root = TreeNode(pre[0])  # 创建根节点
    i = tin.index(pre[0])  # 检索根节点在中序序列中的位置
    # 构建左子树。pre的1~i为左子树，tin的0~i-1为左子树
    # 注意：[start,end] 不包含end
    root.left = pre_in_build_tree(pre[1:i + 1], tin[:i])
    # 构建右子树
    root.right = pre_in_build_tree(pre[i + 1:], tin[i + 1:])
    return root


def bfs_build_tree(bfs_li):
    if not bfs_li or len(bfs_li) < 1:
        return None
    root = TreeNode(bfs_li.pop(0))
    nodes = [root]
    while bfs_li:
        cur = nodes.pop(0)
        node = TreeNode(bfs_li.pop(0))
        cur.left = node
        nodes.append(node)
        if bfs_li:
            node = TreeNode(bfs_li.pop(0))
            cur.right = node
            nodes.append(node)
    return root


def preorder(node):
    if not node:
        return None
    # 先打印根节点信息
    print(node.val, end=" ")
    # 再打印左子树上的所有节点的信息
    preorder(node.left)
    # 最后打印右子树上的所有节点的信息
    preorder(node.right)

def preorder_non_recursive(node):
    """先序遍历的非递归版本"""
    if not node:
        return None
    stack = [node]
    while stack:
        cur_node = stack.pop()
        # 最先打印根节点
        print(cur_node.val, end=" ")
        # 右孩子节点先入栈，后出栈
        if cur_node.right:
            stack.append(cur_node.right)
        # 左孩子节点后入栈，先出栈
        if cur_node.left:
            stack.append(cur_node.left)

def inorder(node):
    if not node:
        return None
    # 先打印左子树
    inorder(node.left)
    # 再打印根节点
    print(node.val, end=" ")
    # 最后打印右子树
    inorder(node.right)

def inorder_non_recursive(node):
    """中序遍历的非递归版本"""
    if not node:
        return None
    stack = []
    cur_node = node
    while cur_node or stack:
        if cur_node:
            # 先一路找到最左子节点
            stack.append(cur_node)
            cur_node = cur_node.left
        else:
            cur_node = stack.pop()
            print(cur_node.val, end=" ")
            cur_node = cur_node.right

def postorder(node):
    # 递归终止条件
    if not node:
        return None
    # 先打印左子树
    postorder(node.left)
    # 再打印右子树
    postorder(node.right)
    # 最后打印根节点
    print(node.val, end=" ")

def postorder_non_recursive(node):
    """后序遍历的非递归版本。若类似于前序遍历直接写，会有些麻烦，因为这里需要判断节点的访问状态，根节点需要最后出栈。
    转换思路，将后序(左->右->根)看作是(根->右->左)的逆序"""
    if not node:
        return None
    stack = [node]
    res = []
    while stack:
        cur_node = stack.pop()
        # 先打印根节点
        res.append(cur_node.val)
        # 左孩子节点先入栈，后出栈
        if cur_node.left:
            stack.append(cur_node.left)
        # 右孩子节点后入栈，先出栈
        if cur_node.right:
            stack.append(cur_node.right)
    # res.reverse()
    # return res
    while res:
        print(res.pop(), end=" ")

def bfs_travel(root):
    "广度优先使用队列，深度优先使用递归或栈"
    if not root:
        return None
    nodes = [root]
    while nodes:
        cur = nodes.pop(0)
        print(cur.val, end=" ")
        if cur.left:
            nodes.append(cur.left)
        if cur.right:
            nodes.append(cur.right)
