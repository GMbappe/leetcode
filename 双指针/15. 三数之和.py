# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 14:48
# @Author  : Guo 
# @File    : 15. 三数之和.py
# @Desc    : https://leetcode-cn.com/problems/3sum/

"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
"""


class Solution:
    def threeSum(self, nums):
        """
        为了不重复，可以先进行排序
        开始最外层循环，找寻第一个数字，第二层循环要比第一层循环大，第三层同理
        并且每一层循环都不要出现重复数字
        在第二层和第三层的时候，可以使用双指针法降低时间复杂度
        左指针是第二层
        右指针是第三层循环，每次递减
        """
        if not nums:
            return []

        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = 0 - nums[i]
            r = n - 1
            for l in range(i + 1, n):
                if l > i + 1 and nums[l] == nums[l - 1]:
                    continue
                while l < r and nums[l] + nums[r] > target:
                    r -= 1
                if l == r:
                    break
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
        return res
