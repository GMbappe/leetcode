# _*_coding:utf-8 _*_
# @Time    : 2021/4/10 19:40
# @Author  : Guo 
# @File    : 263. 丑数.py
# @Desc    : https://leetcode-cn.com/problems/ugly-number/

"""
给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。
丑数 就是只包含质因数 2、3 和/或 5 的正整数。

示例 1：
输入：n = 6
输出：true
解释：6 = 2 × 3

示例 2：
输入：n = 8
输出：true
解释：8 = 2 × 2 × 2
"""


class Solution:
    def isUgly(self, n):
        """
        n = 2a * 3b * 5c
        如果a = b = c = 0 则n=1
        一个数字如果能整除2或3或5，则一直除
        最后判断是否n==1
        """
        if n <= 0:
            return False

        for i in [2, 3, 5]:
            while n % i == 0:
                n = n // i

        return n == 1