# _*_coding:utf-8 _*_
# @Time    : 2021/6/15 19:05
# @Author  : Guo 
# @File    : 105. 从前序与中序遍历序列构造二叉树.py
# @Desc    : https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
根据一棵树的前序遍历与中序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

例如，给出
前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        def helper(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
                return None

            pre_root = pre_left
            in_index = in_map[preorder[pre_root]]  # 根节点在中序的索引位置

            root = TreeNode(preorder[pre_root])  # 创建树
            # 左子树的的节点长度
            subtree = in_index - in_left  #
            root.left = helper(pre_root + 1, pre_root + subtree, in_left, in_index - 1)
            root.right = helper(pre_root + subtree + 1, pre_right, in_index + 1, in_right)

            return root

        in_map = dict()
        n = len(preorder)
        # 中序遍历，每个节点的索引
        for k, v in enumerate(inorder):
            in_map[v] = k

        return helper(0, n - 1, 0, n - 1)