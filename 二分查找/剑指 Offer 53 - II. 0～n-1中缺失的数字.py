# _*_coding:utf-8 _*_
# @Time    : 2022/8/6 22:11
# @Author  : Guo 
# @File    : 剑指 Offer 53 - II. 0～n-1中缺失的数字.py
# @Desc    :
"""
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。 

示例 1:
输入: [0,1,3]
输出: 2

示例 2:
输入: [0,1,2,3,4,5,6,7,9]
输出: 8
"""
class Solution:
    def missingNumber(self, nums) -> int:
        """
        二分查找，如果nums[索引] = 索引
        那么缺失的肯定在其右边  则 l+1
        如果不等那么肯定在其左边 则 r - 1
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m:
                i = m + 1
            else:
                j = m - 1
        return i
