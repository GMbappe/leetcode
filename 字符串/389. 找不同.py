# _*_coding:utf-8 _*_
# @Time    : 2020/12/18 0:47
# @Author  : Guo 
# @File    : 389. 找不同.py
# @Desc    : https://leetcode-cn.com/problems/find-the-difference/

"""
给定两个字符串 s 和 t，它们只包含小写字母。
字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
请找出在 t 中被添加的字母。

示例 1：
输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

示例 2：
输入：s = "", t = "y"
输出："y"
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        双指针，分别指向各自字符串，
        开始遍历，如果遇到不同，则返回t[i]
        如果一直相同，则最后直接输出t[j]
        """
        s = sorted(s)
        t = sorted(t)

        i = 0
        j = 0
        m = len(s)
        n = len(t)
        while i < m and j < n:
            if s[i] != t[j]:
                return t[j]
            i += 1
            j += 1

        if i == m:
            return t[j]