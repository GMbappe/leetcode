# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 21:35
# @Author  : Guo 
# @File    : 75. 颜色分类.py
# @Desc    : https://leetcode-cn.com/problems/sort-colors/

"""
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。


示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
"""


class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        双指针 
        z = 0 表示0的最右边
        t = right 表示2的最左边
        """

        n = len(nums)
        z = 0
        t = n - 1
        i = 0  # 表示1的最右边
        while i <= t:
            if nums[i] == 0:  # 合0交换
                nums[i], nums[z] = nums[z], nums[i]
                i += 1
                z += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[t] = nums[t], nums[i]
                t -= 1