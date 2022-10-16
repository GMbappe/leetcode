# _*_coding:utf-8 _*_
# @Time    : 2021/4/11 23:10
# @Author  : Guo 
# @File    : 264. 丑数 II.py
# @Desc    : https://leetcode-cn.com/problems/ugly-number-ii/
"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。


示例 1：
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：
输入：n = 1
输出：1
解释：1 通常被视为丑数。
"""


class Solution:
    def nthUglyNumber(self, n) -> int:
        """
        p2 代表乘2的，p3代表乘3的，p5代表乘5的 指针
        定义三个指针 p_2,p_3,p_5p
        表示下一个丑数是当前指针指向的丑数乘以对应的质因数。初始时，三个指针的值都是1
        dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
        每次都是和dp[p2] * 2, dp[p3]*3, dp[p5]*5 比较去除最低的
        分别比较如果相等，则相应的指针要挪动一位
        """
        dp = [0] * (n+1)
        dp[1] = 1
        p2 = 1
        p3 = 1
        p5 = 1
        for i in range(2, n+1):
            num1 = dp[p2] * 2
            num2 = dp[p3] * 3
            num3 = dp[p5] * 5
            dp[i] = min(num1, num2, num3)
            if dp[i] == num1:
                p2 += 1
            if dp[i] == num2:
                p3 += 1
            if dp[i] == num3:
                p5 += 1

        return dp[n]