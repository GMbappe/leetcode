# _*_coding:utf-8 _*_
# @Time    : 2021/3/27 23:44
# @Author  : Guo 
# @File    : 3. 无重复字符的最长子串.py
# @Desc    : https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        左指针 就是每次字符的起点，右指针进行移动，直到出现在集合中出现过的，然后左指针移动，并且集合中删除存在的元素
        每次比较最大的长度
        :param s:
        :return:
        """
        if not s:
            return 0
        r = -1
        a = set() # 查询是否有重复
        n = len(s)
        i = 0
        max_len = 1
        while i < n:
            if i > 0 and a: #说明移动了 需要剔除之前存在的
                a.remove(s[i-1])
            while r+1 < n and s[r+1] not in a:  #移动右指针直到不满足条件
                a.add(s[r+1])
                r += 1
            max_len = max(max_len, r+1-i)  # 获取最大长度

            i += 1  # 移动指针
        return max_len