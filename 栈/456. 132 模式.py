# _*_coding:utf-8 _*_
# @Time    : 2021/3/24 21:21
# @Author  : Guo 
# @File    : 456. 132 模式.py
# @Desc    : https://leetcode-cn.com/problems/132-pattern/

"""
给你一个整数数组 nums ，数组中共有 n 个整数。132 模式的子序列 由三个整数 nums[i]、nums[j] 和 nums[k] 组成，
并同时满足：i < j < k 和 nums[i] < nums[k] < nums[j] 。
如果 nums 中存在 132 模式的子序列 ，返回 true ；否则，返回 false 。
进阶：很容易想到时间复杂度为 O(n^2) 的解决方案，你可以设计一个时间复杂度为 O(n logn) 或 O(n) 的解决方案吗？


示例 1：
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列
示例 2：
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
"""

import math


class Solution(object):
    def find132pattern(self, nums):
        """
        1. 从右向左遍历，首先维护一个单调栈，栈顶元素表示当前最大值，然后维护一个次打的值k
        (j,k) 左边如果存在一个值小于k，则说明存在 i<k<j的数字 因为j的数字是在k之后出现的所以索引必比k小
        :param nums:  数组
        :return: boolean
        """
        k = -math.inf
        stack = []
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])

        return False







