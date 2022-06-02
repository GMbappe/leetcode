# _*_coding:utf-8 _*_
# @Time    : 2022/5/14 17:37
# @Author  : Guo 
# @File    : 416. 分割等和子集.py
# @Desc    :https://leetcode.cn/problems/partition-equal-subset-sum/
"""
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等
示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
"""


class Solution:
    def canPartition(self, nums) -> bool:
        """
        dp[i][j] 下标截至到i 是否和为j的情况
        if j >= nums[i]: 两种情况 选或者不选  选的话 则 dp[i-1][j-nums(i)]  不选则 dp[i-1][j] 其中一个为True即可
        else j < nums[i]: 指定不能选  dp[i-1][j]
        特殊情况 dp[i][0] = True dp[0][nums[0]] = True
        """
        n = len(nums)
        if n < 2:  # 如果为长度小于2则不可能拆分
            return False

        sum_ = sum(nums)
        max_num = max(nums)
        if sum_ % 2 == 1:  # 和为奇数也不行拆分
            return False
        half_sum = sum_ // 2  # 拆为两分则 目标就是和的一半
        if max_num > half_sum:  # 最大数超过 和一半 则不可能拆分
            return False

        dp = [[False] * (half_sum + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        dp[0][nums[0]] = True
        for i in range(n):
            for j in range(1, half_sum + 1):
                if nums[i] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n - 1][half_sum]