# _*_coding:utf-8 _*_
# @Time    : 2022/5/10 22:39
# @Author  : Guo 
# @File    : 337. 打家劫舍 III.py
# @Desc    : https://leetcode.cn/problems/house-robber-iii/
"""
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为 root 。
除了 root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的房子在同一天晚上被打劫 ，房屋将自动报警。
给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。


示例 1:
输入: root = [3,2,3,null,3,null,1]
输出: 7
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root):
        """
        dp
        # 此节点被偷，那么他的左右子节点 不能被投
        f[r] = g(l) + g(r) + r.val  当前节点最大值是 左右子节点不被偷和 + 当前节点值
        # 此节点不被偷，那么左右子节点都可以被投或者不被投
        g(r) = max(g(l), f(l)) + max(g(r), f(r))

        但是python的字典 key不能是对象，只能是不可变 类如字符串，数字等
        """

        def DFS(root):
            if not root:
                return 0, 0
            # 后序遍历
            leftchild_steal, leftchild_nosteal = DFS(root.left)
            rightchild_steal, rightchild_nosteal = DFS(root.right)

            # 偷当前node，则最大收益为【投当前节点+不偷左右子树】
            steal = root.val + leftchild_nosteal + rightchild_nosteal
            # 不偷当前node，则可以偷左右子树
            nosteal = max(leftchild_steal, leftchild_nosteal) + max(rightchild_steal, rightchild_nosteal)
            return steal, nosteal

        return max(DFS(root))