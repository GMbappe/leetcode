# _*_coding:utf-8 _*_
# @Time    : 2021/4/23 10:11
# @Author  : Guo 
# @File    : 368. 最大整除子集.py
# @Desc    : https://leetcode-cn.com/problems/largest-divisible-subset/

"""
给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[j]) 都应当满足：
answer[i] % answer[j] == 0 ，或
answer[j] % answer[i] == 0
如果存在多个有效解子集，返回其中任何一个均可。

示例 1：
输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案
"""


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        首先排序
        dp[i] = max(dp[i], dp[j]+1) if j和i整除，并且 0<j<i
        算出每个数字对应的最大整除子集数目，然后倒序进行计算，把符合条件的数字添加进来
        """
        if not nums:
            return 0
        nums.sort()
        n = len(nums)
        dp = [1] * n
        dp[0] = 1
        max_size = 1  # 最大长度
        max_num = nums[0]  # 符合条件的子集最大的数字

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)

            if dp[i] > max_size:
                max_size = dp[i]
                max_num = nums[i]

        if max_size == 1:
            return [nums[0]]

        res = []
        for i in range(n - 1, -1, -1):  # 倒序检查
            if dp[i] == max_size and max_num % nums[i] == 0 and max_size > 0:
                res.append(nums[i])
                max_num = nums[i]
                max_size -= 1

        return res[::-1]