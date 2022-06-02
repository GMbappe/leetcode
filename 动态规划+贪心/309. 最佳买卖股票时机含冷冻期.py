# _*_coding:utf-8 _*_
# @Time    : 2022/5/10 21:23
# @Author  : Guo 
# @File    : 309. 最佳买卖股票时机含冷冻期.py
# @Desc    :

"""
给定一个整数数组prices，其中第  prices[i] 表示第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。


示例 1:
输入: prices = [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
"""


class Solution:
    def maxProfit(self, prices):
        """
        # 第N天是卖出状态所得到的利润
        dp[n][0] = dp[n-1][1]+ price[n]
        # 第N天是买入状态所得到的利润 max(本身就是持有状态，当天买入)
        dp[n][1] = max(dp[n-1][2]-price[n], dp[n-1][1])
        # 第N天是冷冻期所得到的利润 max (前一天卖出状态，前一天冷冻状态)
        dp[n][2] = max(dp[n-1][0], dp[n-1][2])

        最终是三者取大
        """
        n = len(prices)
        dp = [[0 for _ in range(3)] for _ in range(n)]
        # 起始状态
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0

        for i in range(1, n):
            dp[i][0] = dp[i - 1][1] + prices[i]
            dp[i][1] = max(dp[i - 1][2] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][0], dp[i - 1][2])

        return max(dp[-1])
