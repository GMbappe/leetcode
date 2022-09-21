# _*_coding:utf-8 _*_
# @Time    : 2022/8/22 20:29
# @Author  : Guo 
# @File    : 剑指 Offer 33. 二叉搜索树的后序遍历序列.py
# @Desc    :
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3

示例 1：
输入: [1,6,3,2,5]
输出: false
"""


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        """
        二叉搜索树 左子树节点<根节点< 右子树节点
        所以又因为后序遍历，根节点是最后一个，
        首先找到第一个比根节点大的数，就是右子树开始，然后向后如果有比根节点小的则返回False
        """
        return self.helper(0, len(postorder) - 1, postorder)

    def helper(self, left, right, postorder):
        if left > right:
            return True
        root = postorder[right]
        mid = left
        while postorder[mid] < root:  # 找到第一个大于根节点的
            mid += 1
        tmp = mid
        while tmp < right:  # 寻找是否有小于根节点的
            tmp += 1
            if postorder[tmp] < root:
                return False
        return self.helper(left, mid - 1, postorder) and self.helper(mid, right - 1, postorder)