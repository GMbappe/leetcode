# _*_coding:utf-8 _*_
# @Time    : 2021/6/3 23:47
# @Author  : Guo 
# @File    : 525. 连续数组.py
# @Desc    : https://leetcode-cn.com/problems/contiguous-array/
"""
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。

示例 2:
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
"""


class Solution:
    def findMaxLength(self, nums) -> int:
        """
        1. 前缀和 把0 当作-1  相当于求 和为0的 最长连续数组
        2. 相同前缀和的 索引相减
        3. 前缀和可以 用 count 表示，当遇到1 +1 ；遇到 0 -1
        """
        n = len(nums)
        count = 0
        hashmap = {}   # 规定空的前缀的结束下标为-1，由于空的前缀的元素和为 0
        hashmap[0] = -1
        res = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count -= 1

            if count not in hashmap:
                hashmap[count] = i
            else:
                res = max(res, i - hashmap[count])
        return res
