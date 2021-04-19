# _*_coding:utf-8 _*_
# @Time    : 2021/2/6 17:25
# @Author  : Guo 
# @File    : 1423. 可获得的最大点数.py
# @Desc    : https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards/
"""
几张卡牌 排成一行，每张卡牌都有一个对应的点数。点数由整数数组 cardPoints 给出。
每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 k 张卡牌。
你的点数就是你拿到手中的所有卡牌的点数之和。
给你一个整数数组 cardPoints 和整数 k，请你返回可以获得的最大点数。


示例 1：
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。

示例 2：
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。
"""


class Solution:
    def maxScore(self, cardPoints, k) -> int:
        """
        滑动窗口：
        1. 因为是每次都从开头或末尾取走卡牌，那么剩余的n-k必然是连续的
        2. 创造 n-k的窗口，每次移动一格，之后取最小的窗口中的值，
        3. 用数组所有和 - 最小的和 = k的最大的和
        """
        if not cardPoints or k == 0:
            return 0
        n = len(cardPoints)
        window_size = n - k
        window = sum(cardPoints[:n - k])
        min_dow = window
        for i in range(window_size, n):
            window = window + cardPoints[i] - cardPoints[i - window_size]
            min_dow = min(window, min_dow)

        return sum(cardPoints) - min_dow