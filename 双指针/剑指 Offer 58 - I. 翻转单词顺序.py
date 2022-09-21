# _*_coding:utf-8 _*_
# @Time    : 2022/8/15 15:24
# @Author  : Guo 
# @File    : 剑指 Offer 58 - I. 翻转单词顺序.py
# @Desc    : https://leetcode.cn/problems/fan-zhuan-dan-ci-shun-xu-lcof/
"""
输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。
为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，则输出"student. a am I"。
 

示例 1：
输入: "the sky is blue"
输出: "blue is sky the"

示例 2：
输入: "  hello world!  "
输出: "world! hello"
解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
"""


class Solution:
    def reverseWords(self, s):
        s = s.strip()  # 去掉首位空格
        n = len(s)
        i = j = n - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != " ":  # 找到第一个空格
                i -= 1
            res.append(s[i + 1:j + 1])
            while s[i] == " ":  # 过滤所有空格
                i -= 1
            j = i  # 移动j指到下一个单词末尾

        return ' '.join(res)