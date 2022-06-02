# _*_coding:utf-8 _*_
# @Time    : 2022/5/15 21:06
# @Author  : Guo 
# @File    : 438. 找到字符串中所有字母异位词.py
# @Desc    :

"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

例 1:
输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
"""
"""
https://leetcode.cn/problems/find-all-anagrams-in-a-string/solution/hua-dong-chuang-kou-tong-yong-si-xiang-jie-jue-zi-/
"""


class Solution:
    def findAnagrams(self, s, p):
        """
        双指针
        滑动窗口
        """
        l = 0
        r = 0
        match = 0  # 匹配的字符数
        ans = []
        n = len(s)
        m = len(p)
        window = {}  # 窗口内的字符
        p_map = {}
        for i in p:
            p_map[i] = p_map.get(i, 0) + 1

        while r < n:
            r_s = s[r]  # 移动右指针
            if r_s in p_map:
                window[r_s] = window.get(r_s, 0) + 1
                if window[r_s] == p_map[r_s]:
                    match += 1
            r += 1

            while match >= len(p_map):  # 当匹配数大于等于字符串数目可以开始缩减左边
                if r - l == len(p):
                    ans.append(l)
                l_s = s[l]
                if l_s in p_map:
                    window[l_s] -= 1
                    if window[l_s] < p_map[l_s]:
                        match -= 1
                l += 1
        return ans