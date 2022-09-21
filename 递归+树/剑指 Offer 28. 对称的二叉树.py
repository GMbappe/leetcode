# _*_coding:utf-8 _*_
# @Time    : 2022/8/9 11:10
# @Author  : Guo 
# @File    : 剑指 Offer 28. 对称的二叉树.py
# @Desc    : https://leetcode.cn/problems/dui-cheng-de-er-cha-shu-lcof/
"""
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

 
示例 1：
输入：root = [1,2,2,3,4,4,3]
输出：true
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
                DFS 递归操作
                想到 只要左子树的左节点值等于右子树右节点值 并且 左子树右节点值等于右子树左节点值

                停止条件：
                如果左右子树根节点同时没有，说明都对称，返回True
                如果左子树或者右子树没了，返回False
                如果值不相同返回false
                递归条件 就是 左子树左节点和右子树右节点
        xxxxxxv """
        if not root:
            return True
        def recur(l,r):
            if l is None and r is None:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return recur(l.left,r.right) and recur(l.right,r.left)
        return recur(root.left,root.right)