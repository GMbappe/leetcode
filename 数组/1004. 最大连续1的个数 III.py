# _*_coding:utf-8 _*_
# @Time    : 2021/2/19 17:16
# @Author  : Guo 
# @File    : 1004. 最大连续1的个数 III.py
# @Desc    : https://leetcode-cn.com/problems/max-consecutive-ones-iii/
"""
给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。
返回仅包含 1 的最长（连续）子数组的长度。

示例 1：
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：
[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。

示例 2：
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
"""


class Solution:
    def longestOnes(self, A, K) -> int:
        """
        滑动窗口
        1. 数组中得1认为0 ，0认为1
        2. 维护两个指针，left, right; 数组满足以right截至得前缀和 - 以left截至得前缀和 <= K
           即 p[right] - p[left] <= k
        3. 如果未满足，则左指针前进，每次满足后和之前得长度进行比较
        """
        if not A:
            return 0
        n = len(A)
        l = 0
        l_sum = 0
        r_sum = 0
        ans = 0  # 返回长度
        for r in range(n):
            r_sum += 1 - A[r]
            while r_sum - l_sum > K:
                l_sum += 1 - A[l]
                l += 1
            ans = max(ans, r - l + 1)

        return ans
