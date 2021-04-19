# _*_coding:utf-8 _*_
# @Time    : 2021/3/31 22:50
# @Author  : Guo 
# @File    : 90. 子集 II.py
# @Desc    : https://leetcode-cn.com/problems/subsets-ii/
"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

示例 1：
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
"""


class Solution:
    def subsetsWithDup(self, nums):
        """
        回溯，
        首先排序
        1. 首先[],然后用[]和接下来每个数字进行合并，如果当前数字和上一个相同，则跳过此次循环
        2. 依次类推
        """
        self.stack = []
        nums.sort()
        n = len(nums)
        self.back(0, [], nums, n)
        return self.stack

    def back(self, i, path, nums, n):

        self.stack.append(path[:])

        for j in range(i, n):
            if j > i and nums[j] == nums[j - 1]:
                continue
            path.append(nums[j])
            self.back(j + 1, path, nums, n)
            path.pop()  # 撤销
