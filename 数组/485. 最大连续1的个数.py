# _*_coding:utf-8 _*_
# @Time    : 2021/2/15 10:07
# @Author  : Guo 
# @File    : 485. 最大连续1的个数.py
# @Desc    : https://leetcode-cn.com/problems/max-consecutive-ones/
"""
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        依次遍历即可，遇到1则计数器加1，否则重置计数器

        """
        count = 0
        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                count += 1
            elif nums[i] != 1:
                count = 0
            res = max(res, count)

        return res
