# _*_coding:utf-8 _*_
# @Time    : 2022/8/15 13:05
# @Author  : Guo 
# @File    : 剑指 Offer 57. 和为s的两个数字.py
# @Desc    : https://leetcode.cn/problems/he-wei-sde-liang-ge-shu-zi-lcof/
"""
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

示例 2：
输入：nums = [10,26,30,31,47,60], target = 40
输出：[10,30] 或者 [30,10]
"""
class Solution:
    def twoSum(self, nums, target):
        """
        双指针
        如果大于target 右指针移动 否则左指针移动
        """
        n = len(nums)
        i = 0
        j = n-1
        while i < j:
            if nums[i]+nums[j] == target:
                return [nums[i], nums[j]]
            elif nums[i] + nums[j] < target:
                i+=1
            elif nums[i] + nums[j] > target:
                j-=1