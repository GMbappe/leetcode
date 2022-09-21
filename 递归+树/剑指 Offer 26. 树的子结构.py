# _*_coding:utf-8 _*_
# @Time    : 2022/8/9 10:21
# @Author  : Guo 
# @File    : 剑指 Offer 26. 树的子结构.py
# @Desc    : https://leetcode.cn/problems/shu-de-zi-jie-gou-lcof/
"""
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4 
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：
输入：A = [1,2,3], B = [3,1]
输出：false
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubStructure(self, A, B) -> bool:
        if not A or not B:
            return False

        def recur(A, B):
            if not B:
                return True
            if not A or A.val != B.val:
                return False

            return recur(A.left, B.left) and recur(A.right, B.right)

        return recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)