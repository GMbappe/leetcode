# _*_coding:utf-8 _*_
# @Time    : 2021/6/14 19:00
# @Author  : Guo 
# @File    : 238. 除自身以外数组的乘积.py
# @Desc    : https://leetcode-cn.com/problems/product-of-array-except-self/

"""
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        1. left[i] 表示除了这个数以外左边的乘积
        2. right[i] 表示除了这个数以外右边的乘积
        3. 相乘即可
        """
        n = len(nums)
        if n < 1:
            return []
        l = [1] * n
        r = [1] * n
        for i in range(1, n):
            l[i] = l[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            r[i] = r[i + 1] * nums[i + 1]

        ans = []
        for i in range(n):
            cur = l[i] * r[i]
            ans.append(cur)

        return ans