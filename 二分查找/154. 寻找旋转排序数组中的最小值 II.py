# _*_coding:utf-8 _*_
# @Time    : 2021/4/9 9:50
# @Author  : Guo 
# @File    : 154. 寻找旋转排序数组中的最小值 II.py
# @Desc    : https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。
给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。


示例 1：
输入：nums = [1,3,5]
输出：1

示例 2：
输入：nums = [2,2,2,0,1]
输出：0
"""


class Solution:
    def findMin(self, nums) -> int:
        """
        二分
        mid和右边元素对比
        1. 如果大于右边元素，则说明最小元素在右边，左指针移动
        2. 如果中间元素小于右边， 说明最小元素在左边，右指针移动
        3. 如果中间元素等于右边，则移动右边指针一个位置
        """
        if not nums:
            return 0

        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1

        return nums[l]