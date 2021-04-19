# _*_coding:utf-8 _*_
# @Time    : 2021/4/20 0:46
# @Author  : Guo 
# @File    : 28. 实现 strStr().py
# @Desc    : https://leetcode-cn.com/problems/implement-strstr/
"""
实现 strStr() 函数。
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。
说明：
当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：
输入：haystack = "hello", needle = "ll"
输出：2

示例 2：
输入：haystack = "aaaaa", needle = "bba"
输出：-1
"""


class Solution:
    def strStr(self, haystack, needle):
        """
        1. 双指针，如果i j分别指向needle haystack
          如果相同 则一起移动，如果出现不同，则重置 j需要回到j-i的位置 i = 0
        """
        if not needle:
            return 0

        i = 0
        j = 0
        n = len(haystack)
        m = len(needle)
        res = 0
        while j < n:
            if j < n and haystack[j] == needle[i]:
                i += 1
            else:
                j = j - i  # 一定要先减
                i = 0
            if i == m:  # 说明匹配完成
                return j - i + 1

            j += 1  # 每次移动
        return -1