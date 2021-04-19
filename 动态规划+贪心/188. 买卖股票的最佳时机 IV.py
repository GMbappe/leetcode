# _*_coding:utf-8 _*_
# @Time    : 2020/12/28 23:56
# @Author  : Guo 
# @File    : 188. 买卖股票的最佳时机 IV.py
# @Desc    : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

"""
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：
输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

示例 2：
输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
"""


class Solution:
    def maxProfit(self, k, prices):
        """
        DP
        1. have[i][j]  表示第i天，完成j笔交易的最大利润 并且当前手里持有股票  max(have[i-1][j], nohave[i-1][j] - price[i])
        前一天买的，或者前一天没有当天买了
        nohave[i][j]  表示第i天，完成j笔交易的最大利润 并且当前手里持无股票  max(have[i-1][j-1] + price[i], nohave[i-1][j])
        前一天买的，今天卖了 或者前一天没买
        2. 初始状态 have[0][0] = -price[0]  have[0][1..k] = 很小的数 表示不合法
                   nohvae[0][0] = 0   nohave[0][1...k] = 很小数 表示不合法
        3. 注意点 ，交易次数 k最多等于 天数除2的向下取整  len(price)//2
           因为一次买一次卖算一次交易，所以只需要定义have[i][0] 即可, 光买不算交易？
        """

        if not prices:
            return 0

        n = len(prices)
        k = min(k, n // 2)
        have = [[0] * (k + 1) for _ in range(n)]
        nohave = [[0] * (k + 1) for _ in range(n)]

        have[0][0] = -prices[0]
        nohave[0][0] = 0
        for i in range(1, k + 1):
            have[0][i] = float("-inf")
            nohave[0][i] = float("-inf")

        for i in range(1, n):
            have[i][0] = max(have[i - 1][0], nohave[i - 1][0] - prices[i])
            for j in range(1, k + 1):
                have[i][j] = max(have[i - 1][j], nohave[i - 1][j] - prices[i])
                nohave[i][j] = max(have[i - 1][j - 1] + prices[i], nohave[i - 1][j])

        return max(nohave[n - 1])

if __name__ == '__main__':
    a = [1,2,3,4,5]
    k = 2
    s = Solution()
    print(s.maxProfit(k,a))