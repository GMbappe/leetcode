# _*_coding:utf-8 _*_
# @Time    : 2021/4/13 22:55
# @Author  : Guo 
# @File    : 236. 二叉树的最近公共祖先.py
# @Desc    : https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，
最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


示例 1：
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
"""


class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        停止条件，当不存在root 或者 root等于p或q时，返回root
        遍历左子树 l 遍历右子树r
        如果左右都不存在，则返回null
        如果左边存在，右边不存在，则在左子树 返回left
        如果右边存在，左边不存咋，则在右子树，返回right
        如果左右都存在，则在root
        """
        if not root or root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return
        if not left: return right
        if not right: return left
        return root
