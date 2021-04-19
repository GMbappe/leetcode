# _*_coding:utf-8 _*_
# @Time    : 2020/12/15 9:23
# @Author  : Guo 
# @File    : 94. 二叉树的中序遍历.py
# @Desc    : https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)

        return res

    def inorderTraversal2(self, root):
        res = []
        stack = []

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                tmp = stack.pop()
                res.append(tmp.val)
                root = tmp.right

        return res
