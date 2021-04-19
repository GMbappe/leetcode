# _*_coding:utf-8 _*_
# @Time    : 2021/1/8 9:56
# @Author  : Guo 
# @File    : 189. 旋转数组.py
# @Desc    : https://leetcode-cn.com/problems/rotate-array/
"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

示例 1:
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        翻转数组,
        首先反转全部数组，然后反转前k个，然后再反转后面n-k个
        """
        k = k % len(nums)
        
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)