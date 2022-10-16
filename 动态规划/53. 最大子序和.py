# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 17:32
# @Author  : Guo 
# @File    : 53. 最大子序和.py
# @Desc    : https://leetcode-cn.com/problems/maximum-subarray/

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        """
        对于数组中的每一个数，都会存在自己的最大子序和
        对于每一个自己的最大子序和的动态方程为：dp[n] = max(dp[n],dp[n-1]+n)
        """
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_s = nums[0]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_s = max(max_s, dp[i])

        return max_s