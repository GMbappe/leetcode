# _*_coding:utf-8 _*_
# @Time    : 2022/9/17 10:46
# @Author  : Guo 
# @File    : 1624. 两个相同字符之间的最长子字符串.py
# @Desc    : https://leetcode.cn/problems/largest-substring-between-two-equal-characters/
"""
给你一个字符串 s，请你返回 两个相同字符之间的最长子字符串的长度 ，计算长度时不含这两个字符。如果不存在这样的子字符串，返回 -1 。
子字符串 是字符串中的一个连续字符序列。

示例 1：
输入：s = "aa"
输出：0
解释：最优的子字符串是两个 'a' 之间的空子字符串。

示例 2：
输入：s = "abca"
输出：2
解释：最优的子字符串是 "bc" 。
"""
from collections import defaultdict

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        """
        一次遍历，
        有新的相同字符出现，则计算此次最长字符串
        """
        s_map = defaultdict(list)  # 记录每个字符的索引
        ans = -1
        n = len(s)
        for i in range(n):
            s_map[s[i]].append(i)
            cur_ans = s_map[s[i]][-1] - s_map[s[i]][0] - 1
            ans = max(ans, cur_ans)

        return ans