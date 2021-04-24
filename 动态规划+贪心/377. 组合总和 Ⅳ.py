# _*_coding:utf-8 _*_
# @Time    : 2021/4/24 16:19
# @Author  : Guo 
# @File    : 377. 组合总和 Ⅳ.py
# @Desc    : https://leetcode-cn.com/problems/combination-sum-iv/
"""
给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。
题目数据保证答案符合 32 位整数范围。

示例 1：
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
"""


class Solution:
    def combinationSum4(self, nums, target):
        """
        dp[i] 表示 总和为i的拥有的组合数
        dp[i] = 如果数组中的num小于i 则 直接加上dp[i-num]的组合数
                所以最终等于符合条件的dp[i-num]求和
        dp[0] = 1
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]

        return dp[target]