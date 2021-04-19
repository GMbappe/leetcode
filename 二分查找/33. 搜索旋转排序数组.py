# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 17:15
# @Author  : Guo 
# @File    : 33. 搜索旋转排序数组.py
# @Desc    : https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的索引，否则返回 -1 。


示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
"""


class Solution:
    def search(self, nums, target) -> int:
        "找到有序区间，然后不断在有序区间内搜索target"
        if not nums:
            return -1
        n = len(nums)
        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[l]:  # 中间大于左的，说明左边是升序
                if nums[mid] > target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] < nums[l]:  # 中间小于左边 说明右边升序
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
