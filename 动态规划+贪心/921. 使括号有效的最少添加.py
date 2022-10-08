# _*_coding:utf-8 _*_
# @Time    : 2022/10/6 22:13
# @Author  : Guo 
# @File    : 921. 使括号有效的最少添加.py
# @Desc    : https://leetcode.cn/problems/minimum-add-to-make-parentheses-valid/
"""
只有满足下面几点之一，括号字符串才是有效的：
它是一个空字符串，或者
它可以被写成 AB （A 与 B 连接）, 其中 A 和 B 都是有效字符串，或者
它可以被写作 (A)，其中 A 是有效字符串。
给定一个括号字符串 s ，移动N次，你就可以在字符串的任何位置插入一个括号。
例如，如果 s = "()))" ，你可以插入一个开始括号为 "(()))" 或结束括号为 "())))" 。
返回 为使结果字符串 s 有效而必须添加的最少括号数。

示例 1：
输入：s = "())"
输出：1

示例 2：
输入：s = "((("
输出：3
"""


class Solution:
    def minAddToMakeValid(self, s):
        """
        需要左括号和右括号匹配即可
        贪心
        """
        ans = 0
        left = 0
        for i in s:
            if i == "(":
                left += 1
            elif i == ")" and left > 0:
                left -= 1
            elif i == ")" and left <= 0:
                ans += 1

        return ans + left