# _*_coding:utf-8 _*_
# @Time    : 2022/4/22 22:56
# @Author  : Guo 
# @File    : 396. 旋转函数.py
# @Desc    :
"""
给定一个长度为 n 的整数数组 nums 。
假设 arrk 是数组 nums 顺时针旋转 k 个位置后的数组，我们定义 nums 的 旋转函数  F 为：
F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1]
返回 F(0), F(1), ..., F(n-1)中的最大值 。
生成的测试用例让答案符合 32 位 整数。

 
示例 1:
输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。
"""


class Solution:
    def maxRotateFunction(self, nums) -> int:
        """
        F(0) = sum(num*idx for idx, num in enumerate(nums))
        F(1) = F(0) + sum(nums) - nums[-1]*n
        F(2) = F(1) + sum(nums) - nums[-2]*n
        F(i) = F(i-1) + sum(nums) - nums[-i]*n 状态转移方程都出来了，那就 dp 安排一下

        """
        n = len(nums)
        total = sum(nums)
        dp = [0] * n
        dp[0] = sum(num * idx for idx, num in enumerate(nums))
        for i in range(1, n):
            dp[i] = dp[i - 1] + total - nums[-i] * n
        return max(dp)
