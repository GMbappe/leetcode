# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 17:42
# @Author  : Guo 
# @File    : 55. 跳跃游戏.py
# @Desc    : https://leetcode-cn.com/problems/jump-game/

"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。

示例 1：
输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
"""


class Solution(object):
    def can_Jump(self, nums):
        max_jump = 0  # 能跳到的最大索引
        n = len(nums)
        for i in range(n):
            if i > max_jump:  # 如果索引位置大于能跳到的最大索引，则返回Fasle
                return False
            max_jump = max(max_jump, nums[i] + i)
        return True
