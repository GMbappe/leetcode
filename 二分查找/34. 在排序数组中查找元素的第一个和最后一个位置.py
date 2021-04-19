# _*_coding:utf-8 _*_
# @Time    : 2020/12/1 9:01
# @Author  : Guo 
# @File    : 34. 在排序数组中查找元素的第一个和最后一个位置.py
# @Desc    :
"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]

示例 2：
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]

示例 3：
输入：nums = [], target = 0
输出：[-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        顺序遍历，当遇到target时候，开始继续查找，直到第一个不为target停下
        """
        if not nums:
            return [-1, -1]
        n = len(nums)
        i = 0
        res = []
        while i < n:
            if nums[i] == target:
                res.append(i)
                j = i
                while j < n and nums[j] == target:
                    j += 1
                res.append(j - 1)  # 因为j最后多+1了，所以需要添加时候-1
                return res
            i += 1
        return [-1, -1]


class Solution2:
    def searchRange(self, nums, target):
        if not nums:
            return [-1, -1]
        target_left = self.findLeft(nums, target)
        target_right = self.findright(nums, target)

        return [target_left, target_right]

    def findLeft(self, nums, target):
        "二分查找，然后不断向左边查找"
        n = len(nums)
        left = 0
        right = n - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        if left == len(nums):
            return -1
        if nums[left] != target:
            return -1
        return left

    def findright(self, nums, target):
        n = len(nums)
        left = 0
        right = n  # 关键 向右边界查找时候
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid

        if nums[left - 1] != target:
            return -1
        if left == 0:
            return -1

        return left - 1


if __name__ == '__main__':
    a = Solution2()
    a.findLeft(nums=[1], target=1)
