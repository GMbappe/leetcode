# _*_coding:utf-8 _*_
# @Time    : 2022/8/14 10:39
# @Author  : Guo 
# @File    : 剑指 Offer 46. 把数字翻译成字符串.py
# @Desc    : https://leetcode.cn/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，
1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。
请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。


示例 1:
输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
"""
class Solution:
    def translateNum(self, num: int) -> int:
        """
        dp[i] 截至到第i位，可以有X种翻译
        因为
        dp = dp[i-1]+ dp[i-2] if num[i]nums[i-1]组成的数字可以被翻译，所以必须在 [10,25]区间
        否则 = dp[i-1]
        """
        num = str(num)
        n = len(num)
        dp = [0] * (n+1)
        #特殊条件
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            tmp = num[i-2:i]
            if tmp >= "10" and tmp <= "25":
                dp[i] = dp[i-2] + dp[i-1]
            else:
                dp[i] = dp[i-1]
        return dp[n]
        #方法二 
        #也可以进行空间优化
        # a = 1
        # b = 1
        # for i in range(2,n+1):
        #     tmp = num[i-2:i]
        #     if tmp >= "10" and tmp <= "25":
        #         c = a + b
        #     else:
        #         c= a
        #     b = a
        #     a = c
        # return a