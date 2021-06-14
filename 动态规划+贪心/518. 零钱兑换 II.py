# _*_coding:utf-8 _*_
# @Time    : 2021/6/10 22:34
# @Author  : Guo 
# @File    : 518. 零钱兑换 II.py
# @Desc    : https://leetcode-cn.com/problems/coin-change-2/

"""
给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。 

示例 1:
输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
"""


class Solution:
    def change(self, amount, coins) -> int:
        """
        dp[i]  截至i时的兑换数目种类
        """
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]