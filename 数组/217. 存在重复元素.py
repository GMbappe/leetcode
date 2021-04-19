# _*_coding:utf-8 _*_
# @Time    : 2020/12/13 10:00
# @Author  : Guo 
# @File    : 217. 存在重复元素.py
# @Desc    : https://leetcode-cn.com/problems/contains-duplicate/

"""
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        方法1：排序后，比较相邻元素
        方法2：hashset 如果set存在，则返回Ture 
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False
