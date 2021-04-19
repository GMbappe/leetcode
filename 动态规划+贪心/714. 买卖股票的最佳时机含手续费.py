# _*_coding:utf-8 _*_
# @Time    : 2020/12/17 22:53
# @Author  : Guo 
# @File    : 714. 买卖股票的最佳时机含手续费.py
# @Desc    : https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
"""
定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
返回获得利润的最大值。
注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

示例 1:
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
"""


class Solution(object):
    def max_profit(self, prices, fee):
        """
        dp
        1. 设立两个dp 分别表示第i天持有股票以及没有持有股票的最大利润
        有股票 have[i] =  max(前一天买股票利润, 前一天卖股票利润-今天买价格) = max(have[i-1], nohave[i-1] - price[i])
        没股票 nohave[i] = max(前一天有股票利润+今天卖，前一天无股票利润) = max(have[i-1] + price[i] - fee, nohave[i-1])
        初始状态 have[0] = -price[0] ; nohave[0] = 0
        最后输出，一定是没有持有的大于等于持有的利润
        """
        n = len(prices)
        have = [-prices[0]] + [0] * (n-1)
        nohave = [0] * n
        for i in range(1, n):
            have[i] = max(have[i - 1], nohave[i - 1] - prices[i])
            nohave[i] = max(have[i - 1] + prices[i] - fee, nohave[i - 1])

        return nohave[n-1]


if __name__ == "__main__":
    a = Solution()
    prices = [1, 3, 2, 8, 4, 9]
    fee = 2
    print(a.max_profit(prices, fee))


