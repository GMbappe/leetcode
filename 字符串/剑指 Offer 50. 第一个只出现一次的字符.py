# _*_coding:utf-8 _*_
# @Time    : 2022/8/7 14:03
# @Author  : Guo 
# @File    : 剑指 Offer 50. 第一个只出现一次的字符.py
# @Desc    : https://leetcode.cn/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/
"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例 1:
输入：s = "abaccdeff"
输出：'b'

示例 2:
输入：s = ""
输出：' '
"""
from collections import Counter


class Solution:
    def firstUniqChar(self, s):
        if not s:
            return " "

        c = Counter(s)
        for i in c:
            if c[i] == 1:
                return i
        return " "
