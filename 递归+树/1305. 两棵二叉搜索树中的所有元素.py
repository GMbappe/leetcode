# _*_coding:utf-8 _*_
# @Time    : 2022/5/1 12:38
# @Author  : Guo 
# @File    : 1305. 两棵二叉搜索树中的所有元素.py
# @Desc    :

"""
给你 root1 和 root2 这两棵二叉搜索树。请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

示例 1：
输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        '''
        因为是二叉搜索树 所以中序遍历是升序
        '''
        r1 = []
        r2 = []
        self.mid_dfs(root1, r1)
        self.mid_dfs(root2, r2)
        ans = self.merge_list(r1, r2)
        return ans

    def mid_dfs(self, root, r):
        # 中序遍历 左根右
        if root:
            self.mid_dfs(root.left, r)
            r.append(root.val)
            self.mid_dfs(root.right, r)

    def merge_list(self, l1, l2):
        ans = []
        m = len(l1)
        n = len(l2)
        i = 0
        j = 0
        while i < m and j < n:
            if l1[i] <= l2[j]:
                ans.append(l1[i])
                i += 1
            elif l1[i] > l2[j]:
                ans.append(l2[j])
                j += 1
        if i == m:
            ans.extend(l2[j:])
        if j == n:
            ans.extend(l1[i:])
        return ans