# _*_coding:utf-8 _*_
# @Time    : 2022/6/2 14:34
# @Author  : Guo 
# @File    : 450. 删除二叉搜索树中的节点.py
# @Desc    : https://leetcode.cn/problems/delete-node-in-a-bst/

"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，
并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
一般来说，删除节点可分为两个步骤：
首先找到需要删除的节点；
如果找到了，删除它。
 
示例 1:
输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root, key: int):
        """
        1.如果不存在则返回空
        2.如果节点值大于 key 则继续搜索节点的左子树
        3.如果节点小于key，则 搜索节点的右子树
        4. 如果相等，则分为三种情况
            1. 其无左子，则右子树替换
            2. 其无右子，则左子替换
            3. 左右子都有，则左子树 变为右子树的 左子树，右子树替换原来节点位置
        """
        if not root:
            return None
        if root.val > key:
            root.left =  self.deleteNode(root.left, key)
        elif root.val < key:
            root.right =  self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # 左右子树都存在
            node = root.right
            while node.left:  #寻找将删除的节点的右子树的最左节点
                node = node.left
            node.left = root.left  #右子树的左节点替换为之前的左子树
            root = root.right #欲删除节点的右子顶替其位置，节点被删除
        return root