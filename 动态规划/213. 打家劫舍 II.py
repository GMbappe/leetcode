# _*_coding:utf-8 _*_
# @Time    : 2021/4/15 22:22
# @Author  : Guo 
# @File    : 213. 打家劫舍 II.py
# @Desc    : https://leetcode-cn.com/problems/house-robber-ii/

"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，
这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
"""


class Solution:
    def rob(self, nums) -> int:
        """
        由于首尾项链，所以可以当作两种情况
        1. 第一件偷 nums[:-1]
        2. 第一间不偷 nums[1:]
        dp[i] 代表第i间房子获得的最大金额
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])  # 等于上一件投 和 上上投加这次投

        最终比较两种情况的大小
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        a = self.helper(nums[:-1])
        b = self.helper(nums[1:])
        return max(a, b)

    def helper(self, nums):
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1, n):
            if i == 1:
                dp[i] = max(nums[i], dp[0])
            else:
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[n-1]