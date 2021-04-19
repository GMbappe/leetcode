# _*_coding:utf-8 _*_
# @Time    : 2021/2/7 23:54
# @Author  : Guo 
# @File    : 665. 非递减数列.py
# @Desc    : https://leetcode-cn.com/problems/non-decreasing-array/

"""
给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中所有的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
 
示例 1:
输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
"""


class Solution:
    def checkPossibility(self, nums):
        """
        1. 遍历，数组中只能存在一组 nums[i] > nums[i+1]的
           并且如果将nums[i]修改为 nums[i+1] 并且nums[i+1] < nums[i-1] 也是不成立的,这时候需要修改 nums[i+1] = nums[i]
        """
        count = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count > 1:  # 说明至少存在两组nums[i] > nums[i+1]
                    return False
                if i > 0 and nums[i + 1] < nums[i - 1]:
                    nums[i + 1] = nums[i]

        return True
