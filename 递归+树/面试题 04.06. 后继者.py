# _*_coding:utf-8 _*_
# @Time    : 2022/5/16 15:58
# @Author  : Guo 
# @File    : 面试题 04.06. 后继者.py
# @Desc    :
"""
设计一个算法，找出二叉搜索树中指定节点的“下一个”节点（也即中序后继）。
如果指定节点没有对应的“下一个”节点，则返回null。

示例 1:
输入: root = [2,1,3], p = 1

  2
 / \
1   3

输出: 2

示例 2:
输入: root = [5,3,6,2,4,null,null,1], p = 6

      5
     / \
    3   6
   / \
  2   4
 /
1

输出: null
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        """
        中序遍历 bfs
        """
        stack = []
        pre = None  # 前继节点
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre == p:
                return cur
            pre = cur
            cur = cur.right
        return None