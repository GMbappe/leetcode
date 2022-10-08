# _*_coding:utf-8 _*_
# @Time    : 2022/10/8 21:11
# @Author  : Guo 
# @File    : 870. 优势洗牌.py
# @Desc    : https://leetcode.cn/problems/advantage-shuffle/
"""
给定两个大小相等的数组 nums1 和 nums2，nums1 相对于 nums2 的优势可以用满足 nums1[i] > nums2[i] 的索引 i 的数目来描述。
返回 nums1 的任意排列，使其相对于 nums2 的优势最大化。

示例 1：
输入：nums1 = [2,7,11,15], nums2 = [1,10,4,11]
输出：[2,11,7,15]

示例 2：
输入：nums1 = [12,24,8,32], nums2 = [13,25,32,11]
输出：[24,32,8,12]

"""

class Solution:
    def advantageCount(self, nums1, nums2):
        """
        两个数组进行排序
        分别比较大小
        如果nums1 首数 大于 nums2首数
        则该位置答案，随后左指针向又移动
        否则最大数索引对于位置是该个
        """
        n = len(nums1)
        # 将数组的索引按照数字的大小排序
        id1 = list(range(n))
        id2 = list(range(n))
        id1.sort(key=lambda x:nums1[x])
        id2.sort(key=lambda x:nums2[x])

        # 进行顺序比较
        left = 0
        right = n-1
        ans = [0] * n
        for i in range(n):
            if nums1[id1[i]] > nums2[id2[left]]:
                ans[id2[left]] = nums1[id1[i]]
                left += 1
            else:
                ans[id2[right]] = nums1[id1[i]]
                right -= 1
        return ans