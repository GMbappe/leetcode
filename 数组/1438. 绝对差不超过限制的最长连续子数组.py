# _*_coding:utf-8 _*_
# @Time    : 2021/2/21 12:21
# @Author  : Guo 
# @File    : 1438. 绝对差不超过限制的最长连续子数组.py
# @Desc    : https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

"""
给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。
如果不存在满足条件的子数组，则返回 0 。

示例 1：
输入：nums = [8,2,4,7], limit = 4
输出：2
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4.
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4.
因此，满足题意的最长子数组的长度为 2 。
"""

from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums, limit) -> int:
        """
        1. 算以每个数字为数组右端得符合条件得最长连续数组
        2. 顺序遍历，每次右边移动，其左边也会移动
        """
        s = SortedList()
        n = len(nums)
        l = 0
        r = 0
        res = 0
        while r < n:
            s.add(nums[r])
            while s[-1] - s[0] > limit:
                s.remove(nums[l])
                l += 1
            res = max(res, r-l+1)
            r += 1
        return res