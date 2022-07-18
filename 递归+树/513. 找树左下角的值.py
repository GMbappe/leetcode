# _*_coding:utf-8 _*_
# @Time    : 2022/6/22 10:55
# @Author  : Guo 
# @File    : 513. 找树左下角的值.py
# @Desc    : https://leetcode.cn/problems/find-bottom-left-tree-value/

"""
给定一个二叉树的 根节点 root，请找出该二叉树的 最底层 最左边 节点的值。
假设二叉树中至少有一个节点。


示例 1:
输入: root = [2,1,3]
输出: 1
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def findBottomLeftValue(self, root) -> int:
        # 层次遍历 找到最后一层 然后最后一层第一个节点为 左边节点
        if not root:
            return None

        queue = deque([root])
        ans = []
        while queue:
            n = len(queue)
            cur_ans = []
            for _ in range(n):
                d = queue.popleft()
                cur_ans.append(d.val)
                if d.left:
                    queue.append(d.left)
                if d.right:
                    queue.append(d.right)
            ans = cur_ans
        return ans[0]
