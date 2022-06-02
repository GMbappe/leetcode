# _*_coding:utf-8 _*_
# @Time    : 2022/5/14 17:57
# @Author  : Guo 
# @File    : 437. 路径总和 III.py
# @Desc    : https://leetcode.cn/problems/path-sum-iii/

"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum) -> int:
        if not root:
            return 0
        ret = 0
        ret += self.dfs(root, targetSum)
        ret += self.pathSum(root.left, targetSum)  # 循环对左子树和右子树递归
        ret += self.pathSum(root.right, targetSum)
        return ret

    def dfs(self, root, targetSum):
        if not root:
            return 0

        ret = 0
        if root.val == targetSum:
            ret += 1
        ret += self.dfs(root.left, targetSum - root.val)
        ret += self.dfs(root.right, targetSum - root.val)
        return ret
