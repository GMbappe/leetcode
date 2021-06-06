# _*_coding:utf-8 _*_
# @Time    : 2021/6/3 23:49
# @Author  : Guo 
# @File    : 523. 连续的子数组和.py
# @Desc    : https://leetcode-cn.com/problems/continuous-subarray-sum/

"""
给你一个整数数组 nums 和一个整数 k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
子数组大小 至少为 2 ，且
子数组元素总和为 k 的倍数。
如果存在，返回 true ；否则，返回 false 。
如果存在一个整数 n ，令整数 x 符合 x = n * k ，则称 x 是 k 的一个倍数。


示例 1：
输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
"""


class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        """
        1. 前缀和
        2. 遇到相同余数的 相减即可，所以可以用hashmap保存余数，当遇到相同余数时候，比较是否是两个满足两个子数组
        """
        if not nums:
            return False

        n = len(nums)
        if n < 2:
            return False
        res = [0] * (n + 1)
        for i in range(1, n + 1):  # 前缀和
            res[i] = res[i - 1] + nums[i - 1]

        print(res)
        hashmap = {}
        for i in range(n + 1):
            cur = res[i] % k
            if cur in hashmap:
                if i - hashmap[cur] >= 2:
                    return True
            else:
                hashmap[cur] = i
        return False