# _*_coding:utf-8 _*_
# @Time    : 2020/12/30 0:37
# @Author  : Guo 
# @File    : 330. 按要求补齐数组.py
# @Desc    : https://leetcode-cn.com/problems/patching-array/
"""
给定一个已排序的正整数数组 nums，和一个正整数 n 。从 [1, n] 区间内选取任意个数字补充到 nums 中，
使得 [1, n] 区间内的任何数字都可以用 nums 中某几个数字的和来表示。请输出满足上述要求的最少需要补充的数字个数。


示例 1:
输入: nums = [1,3], n = 6
输出: 1
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。

示例 2:
输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2, 4]。
"""


class Solution(object):
    def minPatches(self, nums, n):
        """
        如果 [1, x-1] 被覆盖，那么 [1,2x-1] 也同样被覆盖
        假射 x初始是1 如果 数组第一个元素 <= x 则表示[1, x-1] 已经被覆盖完，那么直接更新 x [1, x + nums[index] -1]
        否则 如果 > x : 说明[1, x-1] 没有被覆盖完， 直接添加x , 然后更新 x *2
        """
        count = 0
        x = 1
        i = 0  # 数组索引
        l = len(nums)
        while x <= n:
            if i < l and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                x *= 2
                count += 1
        return count
