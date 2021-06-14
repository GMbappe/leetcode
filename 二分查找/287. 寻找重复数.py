# _*_coding:utf-8 _*_
# @Time    : 2021/6/14 19:31
# @Author  : Guo 
# @File    : 287. 寻找重复数.py
# @Desc    : https://leetcode-cn.com/problems/find-the-duplicate-number/'

"""
给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。
假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。
你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。

示例 1：
输入：nums = [1,3,4,2,2]
输出：2

示例 2：
输入：nums = [3,1,3,4,2]
输出：3
"""


class Solution:
    def findDuplicate(self, nums) -> int:
        """
        二分查找，查找1到n(数组长度-1)
        如果小于Mid数字出现次数大于mid 则说明重复数字一定出现是小于等于mid里面的数
        """
        left = 1
        right = len(nums) - 1
        while left < right:
            mid = left+(right-left)//2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt +=1
            if cnt > mid:
                right = mid
            else:
                left = mid +1
        return left