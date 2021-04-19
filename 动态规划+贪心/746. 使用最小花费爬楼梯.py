# _*_coding:utf-8 _*_
# @Time    : 2020/12/21 22:09
# @Author  : Guo 
# @File    : 746. 使用最小花费爬楼梯.py
# @Desc    : https://leetcode-cn.com/problems/min-cost-climbing-stairs/

"""
数组的每个索引作为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

 示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
"""


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        dp
        dp[n] 表示爬到当前楼需要的最小力气
        转移方程 dp[n] = min(dp[n-2] + cost[n-2], dp[n-1] + cost[n-1])
        初始： dp[0] = 0 dp[1] = 1
        """
        if not cost:
            return 0

        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1])

        return dp[n]