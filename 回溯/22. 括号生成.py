# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 17:54
# @Author  : Guo 
# @File    : 22. 括号生成.py
# @Desc    : https://leetcode-cn.com/problems/generate-parentheses/

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

示例 1：
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""


class Solution:
    def generateParenthesis(self, n: int):
        self.stack = []
        self.helper("", n, n)
        return self.stack

    def helper(self, s, l, r):
        """
        如果左括号数目>0 则可以向左分支继续分支，
        如果左括号数目小于右括号数目，可以向右分支
        如果左括号数目严格大于右括号，则必须剪枝 return
        当左右数目都为0时，则添加
        """
        if l == 0 and r == 0:
            self.stack.append(s)
        if l > r:
            return
        if r > 0:
            self.helper(s + ")", l, r - 1)
        if l > 0:
            self.helper(s + "(", l - 1, r)
