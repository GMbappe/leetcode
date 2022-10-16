# _*_coding:utf-8 _*_
# @Time    : 2021/5/16 19:08
# @Author  : Guo 
# @File    : 152. 乘积最大子数组.py
# @Desc    : https://leetcode-cn.com/problems/maximum-product-subarray/

"""
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
"""


class Solution:
    def maxProduct(self, nums):
        """
        dp
        因为存在负数，所以开两个动态数组
        一个是截至当前最大
        一个是截至当前最小
        dp_max[i] = max(dp_max[i-1]*num, dp_min[i-1]*num, num)
        dp_min[i] = min(dp_min[i-1]*num, dp_max[i-1]*num,num)
        ans = max(dp_max, ans)
        """
        if not nums:
            return 0
        n = len(nums)
        dp_max = [nums[0]] + (n-1)*[0]
        dp_min = [nums[0]] + (n-1)*[0]
        ans = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            dp_min[i] = min(dp_max[i-1]*nums[i], dp_min[i-1]*nums[i], nums[i])
            ans = max(dp_max[i], ans)
        return ans