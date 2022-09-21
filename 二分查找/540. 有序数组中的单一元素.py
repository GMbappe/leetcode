# _*_coding:utf-8 _*_
# @Time    : 2022/8/9 22:06
# @Author  : Guo 
# @File    : 540. 有序数组中的单一元素.py
# @Desc    : https://leetcode.cn/problems/single-element-in-a-sorted-array/
"""
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。


示例 1:
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

示例 2:
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
"""


class Solution:
    def singleNonDuplicate(self, nums) -> int:
        """
        二分：
        因为只有一个元素是出现一次，那么我们可以用二分进行,正常出现是[偶数，奇数]
        如果mid 是奇数 那么 nums[mid] = nums[mid-1] 那么说明前半段没有缺失，在后半段
        如果mid是偶数 那么如果nums[mid] = nums[mid+1]说明前半段没有缺失，在后半段
        """
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    l = mid + 1
                else:
                    r = mid
            elif mid % 2 != 0:
                if nums[mid] == nums[mid - 1]:
                    l = mid + 1
                else:
                    r = mid

        return nums[l]