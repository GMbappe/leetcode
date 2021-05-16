# _*_coding:utf-8 _*_
# @Time    : 2021/5/16 15:41
# @Author  : Guo 
# @File    : 102. 二叉树的层序遍历.py
# @Desc    : https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。


示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层序遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            cur = []
            next_node = []
            for node in stack:
                if node:
                    cur.append(node.val)
                if node.left:
                    next_node.append(node.left)
                if node.right:
                    next_node.append(node.right)
            res.append(cur)
            stack = next_node
        return res