# _*_coding:utf-8 _*_
# @Time    : 2020/12/15 9:35
# @Author  : Guo 
# @File    : 912. 排序数组.py
# @Desc    : https://leetcode-cn.com/problems/sort-an-array/
"""
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""


class Solution(object):
    def fast_sort(self, nums):
        """
        快速排序思想
        找到一个哨兵，然后依次找到比他大的数字放到右边，找到比他小的数字放到左边，然后再从各自区间继续寻找，循环
        """
        n = len(nums)

        def quick(left, right):
            if left >= right:
                return nums
            pivot = left  # 哨兵
            i = left
            j = right
            while i < j:
                while i < j and nums[j] > nums[pivot]:  # 右边开始找到第一个比哨兵小的
                    j -= 1
                while i < j and nums[i] <= nums[pivot]:  # 左边找到第一个比哨兵大的
                    i += 1
                nums[i], nums[j] = nums[j], nums[i]  # 换位置 小的来左边 大的去右边
            nums[pivot], nums[j] = nums[j], nums[pivot]  # 交换哨兵的位置
            quick(left, j - 1)
            quick(j + 1, right)

            return nums

        return quick(0, n - 1)

    def merge_sort(self, nums):
        """
        归并排序
        不断拆分，直到剩下一个数字，
        然后开始比较数字大小进行合并
        """
        if len(nums) <= 1:   # 分割终止条件
            return nums
        mid = len(nums)//2  # 分
        nums1 = self.merge_sort(nums[:mid])  # 分
        nums2 = self.merge_sort(nums[mid:])
        return self.merge(nums1, nums2)

    def merge(self, nums1, nums2):
        """
        合并 nums1 和 nums2
        """
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        res = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                res.append(nums2[j])
                j += 1
        if i == m:  # 说明nums1数组已经全部添加，直接添加nums2剩余的即可
            res.extend(nums2[j:])
        if j == n:
            res.extend(nums1[i:])
        return res

