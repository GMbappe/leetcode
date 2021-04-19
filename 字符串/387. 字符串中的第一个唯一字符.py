# _*_coding:utf-8 _*_
# @Time    : 2020/12/23 0:16
# @Author  : Guo 
# @File    : 387. 字符串中的第一个唯一字符.py
# @Desc    : https://leetcode-cn.com/problems/first-unique-character-in-a-string/

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

示例：
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        1. 首先统计字符出现次数 用 hashmap
        2. 然后遍历字符串，如果出现次数为1 则返回索引  否则返回-1
        """
        s_counts = {}
        for i in s:
            s_counts[i] = s_counts.get(i, 0) + 1

        n = len(s)
        for j in range(n):
            if s_counts[s[j]] == 1:
                return j
        return -1