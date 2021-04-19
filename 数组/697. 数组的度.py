# _*_coding:utf-8 _*_
# @Time    : 2021/2/20 22:44
# @Author  : Guo 
# @File    : 697. 数组的度.py
# @Desc    : https://leetcode-cn.com/problems/degree-of-an-array/
"""
给定一个非空且只包含非负数的整数数组 nums，数组的度的定义是指数组里任一元素出现频数的最大值。
你的任务是在 nums 中找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。

示例 1：
输入：[1, 2, 2, 3, 1]
输出：2
解释：
输入数组的度是2，因为元素1和2的出现频数最大，均为2.
连续子数组里面拥有相同度的有如下所示:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组[2, 2]的长度为2，所以返回2.
"""

import collections
import math


class Solution:
    def findShortestSubArray(self, nums) -> int:
        """
        1. 记录数组中每个数字得左边界和右边界 以及 每个数字出现得次数
        2. 然后分别找出出现次数最多得数字，以及其左右边界
        3. 开始比较，左右边界距离最小得值
        """
        left = {}  # 记录数字左边界
        right = {}  # 记录数字右边界
        count = collections.Counter()  # 记录数字出现次数
        n = len(nums)
        for i in range(n):
            if nums[i] not in left:
                left[nums[i]] = i
            right[nums[i]] = i
            count[nums[i]] += 1
        depth = max(count.values())
        res = math.inf
        for k, v in count.items():
            if v == depth:
                res = min(res, right[k] - left[k] + 1)

        return res

