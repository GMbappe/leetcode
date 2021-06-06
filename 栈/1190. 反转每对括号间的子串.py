# _*_coding:utf-8 _*_
# @Time    : 2021/5/26 23:26
# @Author  : Guo 
# @File    : 1190. 反转每对括号间的子串.py
# @Desc    : https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses/

"""
给出一个字符串 s（仅含有小写英文字母和括号）。
请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。
注意，您的结果中 不应 包含任何括号。

示例 1：
输入：s = "(abcd)"
输出："dcba"

示例 2：
输入：s = "(u(love)i)"
输出："iloveu"
"""


class Solution:
    def reverseParentheses(self, s):
        """
        辅助栈
        1. 如果遇到的不是右括号，则字符串入栈，
        2. 当遇到右括号时候，开始出栈，直到再次遇到左括号，然后把这次的和之前的辅助栈拼接
        """
        if not s:
            return ""

        stack = []
        for i in s:
            if i != ")":
                stack.append(i)
            elif i == ")":
                tmp = []
                while stack and stack[-1] != "(":  # 开始出栈
                    a = stack.pop()
                    tmp.append(a)
                stack.pop()
                stack += tmp
        return "".join(stack)