# _*_coding:utf-8 _*_
# @Time    : 2022/8/10 15:44
# @Author  : Guo 
# @File    : 121. 买卖股票的最佳时机.py
# @Desc    :https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/
"""
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

 
示例 1：
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
"""

class Solution:
    def maxProfit(self, prices) -> int:
        """
        DP
        第i次卖出，则必然在之前的买入
        每次比较当前卖出的价值和之前的最大价值的，选出最大值；每次更新最小买入价格
        """
        max_gap = 0
        min_price = 1e9
        for i in prices:
            max_gap = max(i-min_price,max_gap) #假如卖出能够获得最大利润
            min_price = min(i,min_price) #假如买进的最低点
        return max_gap