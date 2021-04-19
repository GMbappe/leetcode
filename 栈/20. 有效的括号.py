# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 17:08
# @Author  : Guo 
# @File    : 20. 有效的括号.py
# @Desc    : https://leetcode-cn.com/problems/valid-parentheses/

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：
输入：s = "()"
输出：true

示例 2：
输入：s = "()[]{}"
输出：true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        辅助栈
        遇到右括号则从栈中弹出，如果成对 则弹出栈顶元素
        """
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for i in s:
            if i in pairs:
                if not stack or stack[-1] != pairs[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)

        return not stack