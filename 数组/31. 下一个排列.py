# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 22:13
# @Author  : Guo 
# @File    : 31. 下一个排列.py
# @Desc    : https://leetcode-cn.com/problems/next-permutation/

"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。

示例 1：
输入：nums = [1,2,3]
输出：[1,3,2]

示例 2：
输入：nums = [3,2,1]
输出：[1,2,3]
"""


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:  # 找到第一个后面比前面大的
            i -= 1
        if i >= 0:  # 首次扫描如果到达第一个索引，则该序列时最大序列，直接降序即可
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:  # 从后向前，找到第一个比i索引位置大的数字
                j -= 1

            nums[i], nums[j] = nums[j], nums[i]  # 交换
        # i 索引后面的数字重新升序排列, 因为可知i 索引后的数字必为降序
        l = i + 1
        r = n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums
