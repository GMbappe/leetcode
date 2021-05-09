# _*_coding:utf-8 _*_
# @Time    : 2021/5/9 23:16
# @Author  : Guo 
# @File    : 1482. 制作 m 束花所需的最少天数.py
# @Desc    : https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets/

"""
给你一个整数数组 bloomDay，以及两个整数 m 和 k 。
现需要制作 m 束花。制作花束时，需要使用花园中 相邻的 k 朵花 。
花园中有 n 朵花，第 i 朵花会在 bloomDay[i] 时盛开，恰好 可以用于 一束 花中。
请你返回从花园中摘 m 束花需要等待的最少的天数。如果不能摘到 m 束花则返回 -1 。


示例 1：
输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
输出：3
解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
现在需要制作 3 束花，每束只需要 1 朵。
1 天后：[x, _, _, _, _]   // 只能制作 1 束花
2 天后：[x, _, _, _, x]   // 只能制作 2 束花
3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3
"""


class Solution:
    def minDays(self, bloomDay, m, k):
        """
        二分
        1. 首先定义一个函数，算出当前天数能否完成目标
        2. 二分查找天数，区间是数组中的最低和最高；找到最早的那个天数
        """
        n = len(bloomDay)
        if m * k > n:
            return -1

        def canmake(days):
            """
            顺序遍历，如果遇到小于天数的则当前flower+1，如果等于k的话说明可以制作一束，然后重置花朵
            最后输出制作的花是否和m相等
            """
            c = 0
            flower = 0
            for v in bloomDay:
                if v <= days:
                    flower += 1
                    if flower == k:
                        c += 1
                        if c == m:  # 如果达到要求提前结束循环
                            break
                        flower = 0  # 重置
                else:
                    flower = 0
            return c == m

        l = min(bloomDay)
        r = max(bloomDay)
        while l < r:
            mid = (l + r) // 2
            if canmake(mid):  # 说明找到符合条件天数 右指针移动
                r = mid
            else:
                l = mid + 1
        return l
