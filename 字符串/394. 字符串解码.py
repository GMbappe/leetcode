# _*_coding:utf-8 _*_
# @Time    : 2022/5/11 20:18
# @Author  : Guo 
# @File    : 394. 字符串解码.py
# @Desc    :
"""
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例 1：
输入：s = "3[a]2[bc]"
输出："aaabcbc"

示例 2：
输入：s = "3[a2[c]]"
输出："accaccacc"
"""


class Solution:
    def decodeString(self, s):
        """
        辅助栈
        遇到 ] 开始弹出，直到是[ 其中的字符进行拼接
        """
        ans = []
        n = len(s)
        for i in range(n):
            if s[i] == "]":
                s1 = ""
                while ans[-1] != "[":  # 弹出字符进行拼接
                    s1 = ans.pop() + s1
                ans.pop()  # 弹出 [
                n = ''
                while ans and ans[-1].isdigit():
                    n = ans.pop() + n
                s1 = int(n) * s1
                ans.append(s1)
            else:
                ans.append(s[i])

        return ''.join(ans)