# _*_coding:utf-8 _*_
# @Time    : 2022/9/20 12:37
# @Author  : Guo 
# @File    : 698. 划分为k个相等的子集.py
# @Desc    : https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/
"""
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

示例 2:
输入: nums = [1,2,3,4], k = 3
输出: false
"""


class Solution:
    def canPartitionKSubsets(self, nums, k) -> bool:
        if sum(nums) % k != 0:  # 不能整除 返回false
            return False

        target = sum(nums) // k
        nums.sort(reverse=True)  # 降序排列
        n = len(nums)
        bucket = [0] * (k + 1)  # 分成k个桶 表示每个桶的和

        return self.dfs(nums, target, k, 0, n, bucket)

    def dfs(self, nums, target, k, index, n, bucket):
        # 球选桶
        if index == n:  # 当所有球都选完后
            # for i in range(k):
            #     if bucket[i] != target:
            #         return False
            return True

        # 球开始做选择，查看选择哪个框
        for i in range(k):
            if i > 0 and index == 0:  # 第一个球放入任意都行 规定就放第一个
                break
            if bucket[i] + nums[index] > target:
                continue
            if i > 0 and bucket[i] == bucket[i - 1]:  # 如果当前桶和和上一个相同，则选当前桶和上一个结果是一样的
                continue
            bucket[i] += nums[index]  # 球放入第 i 个桶
            if self.dfs(nums, target, k, index + 1, n, bucket):
                return True
            bucket[i] -= nums[index]
        return False





