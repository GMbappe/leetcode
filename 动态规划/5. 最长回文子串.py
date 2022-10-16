# _*_coding:utf-8 _*_
# @Time    : 2020/12/14 23:43
# @Author  : Guo 
# @File    : 5. 最长回文子串.py
# @Desc    : https://leetcode-cn.com/problems/longest-palindromic-substring/
"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        dp[i][j] 为索引i到j字符串是否为回文串
        """
        if len(s) < 2:
            return s

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        max_len = 1
        start = 0

        for i in range(n):  # 单个字符必是回文串
            dp[i][i] = True

        for j in range(1, n):  # 从后到前
            for i in range(j):
                if s[i] == s[j]:  # 如果i到j字符串的子串是回文，那么i到j也是回文， 如何保证子串是回文，小于2 一定是回文
                    if j - 1 - (i + 1) + 1 < 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] is True:
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start = i

        return s[start: start + max_len]


class Solution(object):  # 方法2
    def longestPalindrome(self, s):
        """
        中心扩散法
        以每一个字符为中心，向外扩散，如果符合回文条件就继续扩散
        """
        start = 0
        end = 0
        n = len(s)
        for i in range(s):
            left1, right1 = self.mid(s, i, i)
            left2, right2 = self.mid(s, i, i + 1)
            if right1 - left1 > end - start:
                start = left1
                end = right1
            if right2 - left2 > end - start:
                start = left2
                end = right2

            return s[start: end + 1]

    def mid(self, s, left, right):
        i = left
        j = right
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return i + 1, j - 1


if __name__ == '__main__':
    s = "babad"
    r = Solution()
    print(r.longestPalindrome(s))
