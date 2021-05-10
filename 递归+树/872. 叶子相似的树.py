# _*_coding:utf-8 _*_
# @Time    : 2021/5/10 9:53
# @Author  : Guo 
# @File    : 872. 叶子相似的树.py
# @Desc    : https://leetcode-cn.com/problems/leaf-similar-trees/
"""
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。
如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
如果给定的两个根结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

示例 1：
输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true

示例 2：
输入：root1 = [1], root2 = [1]
输出：true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1, root2):
        """
        直接先dfs得到每棵树的叶结点值 然后比较
        """
        res1 = []
        self.dfs(root1, res1)
        res2 = []
        self.dfs(root2, res2)
        return res1 == res2

    def dfs(self, root, res):
        if not root.left and not root.right:  # 找到叶节点
            res.append(root.val)
        else:
            if root.left:
                self.dfs(root.left, res)
            if root.right:
                self.dfs(root.right, res)