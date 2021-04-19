# _*_coding:utf-8 _*_
# @Time    : 2021/3/11 23:09
# @Author  : Guo 
# @File    : 227. 基本计算器 II.py
# @Desc    : https://leetcode-cn.com/problems/basic-calculator-ii/

"""
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。

示例 1：
输入：s = "3+2*2"
输出：7

示例 2：
输入：s = " 3/2 "
输出：1
"""


class Solution(object):
    def calculate(self, s):
        """
        辅助栈，sign表示数字前的符号
        遇到相应符号做相应的处理，把除了乘除以外数字全部压入栈中，最后求栈中数字之和即可
        遇到新符号时候 需要计算符号前数字
        """
        sign = "+"
        n = len(s)
        stack = []
        num = 0
        for i in range(n):
            if s[i] != " " and s[i].isdigit():
                num = num*10 + ord(s[i]) - ord('0')  #算出当前数字
            if i == n-1 or s[i] in "+-*/":  # 遇到新符号后 需要计算符号的符号，以判断如何操作
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    a = stack.pop()
                    stack.append(a*num)
                else:
                    a = stack.pop()
                    stack.append(int(a/num))
                sign = s[i] # 更新符号
                num = 0 # 遇到新符号 需要重置数字为0

        return sum(stack)


