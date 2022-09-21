# _*_coding:utf-8 _*_
# @Time    : 2022/8/18 16:59
# @Author  : Guo 
# @File    : 209. 长度最小的子数组.py
# @Desc    : https://leetcode.cn/problems/minimum-size-subarray-sum/
"""
给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。

 
示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

示例 2：
输入：target = 4, nums = [1,4,4]
输出：1

示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
"""


class Solution:
    def minSubArrayLen(self, target, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        l = 0
        r = 0
        min_len = n+1
        s_ = 0
        while r < n:
            s_ += nums[r]
            while s_ >= target:
                min_len = min(min_len, r-l+1)
                s_ -= nums[l]  # 左指针移动
                l += 1
            r += 1
        return 0 if min_len == n+1 else min_len