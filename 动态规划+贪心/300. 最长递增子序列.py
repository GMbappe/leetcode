# _*_coding:utf-8 _*_
# @Time    : 2021/6/14 20:52
# @Author  : Guo 
# @File    : 300. 最长递增子序列.py
# @Desc    : https://leetcode-cn.com/problems/longest-increasing-subsequence/

"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
 
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
"""


class Solution:
    def lengthOfLIS(self, nums) -> int:
        """
        dp[i] 表示 截至到第i位的最长上升子序列
        转移方程 dp[i] = max(dp[j] + 1) 0<j<i
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]

        for i in range(len(nums)):
            # 每次更新位置至少一个子序列
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)