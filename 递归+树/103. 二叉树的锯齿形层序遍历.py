# _*_coding:utf-8 _*_
# @Time    : 2020/12/23 0:04
# @Author  : Guo 
# @File    : 103. 二叉树的锯齿形层序遍历.py
# @Desc    :
"""
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层序遍历如下：

[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        stack = [root]
        count = 0

        while stack:
            cur_node = []
            next_node = []
            for i in stack:
                if i:
                    cur_node.append(i.val)
                    next_node.extend([i.left, i.right])
            if cur_node:
                if count % 2 == 0:
                    res.append(cur_node)
                else:
                    res.append(cur_node[::-1])
            count += 1
            stack = next_node
        return res
