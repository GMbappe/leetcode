# _*_coding:utf-8 _*_
# @Time    : 2022/8/5 18:37
# @Author  : Guo 
# @File    : 623. 在二叉树中增加一行.py
# @Desc    : https://leetcode.cn/problems/add-one-row-to-tree/

"""
给定一个二叉树的根 root 和两个整数 val 和 depth ，在给定的深度 depth 处添加一个值为 val 的节点行。
注意，根节点 root 位于深度 1 。

加法规则如下:
给定整数 depth，对于深度为 depth - 1 的每个非空树节点 cur ，创建两个值为 val 的树节点作为 cur 的左子树根和右子树根。
cur 原来的左子树应该是新的左子树根的左子树。
cur 原来的右子树应该是新的右子树根的右子树。
如果 depth == 1 意味着 depth - 1 根本没有深度，那么创建一个树节点，值 val 作为整个原始树的新根，而原始树就是新根的左子树。
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root, val, depth):
        if not root:
            return None
        if depth==1: #深度为1 则之前根节点为左节点
            return TreeNode(val, root, None)
        if depth==2: #深度为2, 则之前在深度1的节点 是改值的左右节点
            root.left = TreeNode(val, root.left,None)
            root.right = TreeNode(val, None, root.right)
        else: #否则就递归 直到是其深度-1
            root.left = self.addOneRow(root.left, val, depth-1)
            root.right = self.addOneRow(root.right, val, depth-1)

        return root