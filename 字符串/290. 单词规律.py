# _*_coding:utf-8 _*_
# @Time    : 2020/12/16 23:32
# @Author  : Guo 
# @File    : 290. 单词规律.py
# @Desc    : https://leetcode-cn.com/problems/word-pattern/
"""
给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:
输入: pattern = "abba", str = "dog cat cat dog"
输出: true

示例 2:
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
"""


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        1. 建立两个map,
        2. 一次进行遍历，然后形成映射关系； 互为映射关系
        3. 如果出现不一致则返回false
        """
        p = dict() 
        w = dict()
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        for pa, word in zip(pattern, words):
            if (pa in p and p[pa] != word) or (word in w and w[word] != pa):  # 如果各自不对应 则直接返回false
                return False
            p[pa] = word
            w[word] = pa

        return True
