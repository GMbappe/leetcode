# _*_coding:utf-8 _*_
# @Time    : 2022/9/21 20:07
# @Author  : Guo 
# @File    : 854. 相似度为 K 的字符串.py
# @Desc    : https://leetcode.cn/problems/k-similar-strings/
"""
对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，
则认为字符串 s1 和 s2 的 相似度为 k 。
给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。

示例 1：
输入：s1 = "ab", s2 = "ba"
输出：1

示例 2：
输入：s1 = "abc", s2 = "bca"
输出：2

"""
from collections import deque

class Solution:
    def kSimilarity(self, s1, s2) -> int:
        """
        bfs 每次比较当前字符，如果相同，则继续，直到第一个不相同，然后和s2后面的字符进行交换
            并且保证，s1[i] == s2[j] and s1[j] != s2[j]
        """
        def next(s):
            i = 0
            while s[i] == s2[i]:
                i += 1
            res = []
            for j in range(i + 1, n):
                if s[j] == s2[i] and s[j] != s2[j]:
                    res.append(s2[: i + 1] + s[i + 1 : j] + s[i] + s[j + 1 :])
            return res

        q = deque([s1])
        vis = {s1}
        ans, n = 0, len(s1)
        while 1:
            for _ in range(len(q)):
                s = q.popleft()
                if s == s2:
                    return ans
                for nxt in next(s):
                    if nxt not in vis:
                        vis.add(nxt)
                        q.append(nxt)
            ans += 1
