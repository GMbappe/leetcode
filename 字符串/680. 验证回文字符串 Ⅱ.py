# _*_coding:utf-8 _*_
# @Time    : 2020/12/18 0:32
# @Author  : Guo 
# @File    : 680. 验证回文字符串 Ⅱ.py
# @Desc    : https://leetcode-cn.com/problems/valid-palindrome-ii/

"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:
输入: "aba"
输出: True

示例 2:
输入: "abca"
输出: True
解释: 你可以删除c字符。
"""


class Solution(object):
    def validPalindrome(self, s):
        """
        双指针， 依次判断，如果相等则继续前进，如果不等，则删除其中一个进行判断
        """
        n = len(s)
        left = 0
        right = n - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.is_huiwen(s[0:left] + s[left + 1:n]) or self.is_huiwen(s[0:right] + s[right + 1:n])
        return True

    def is_huiwen(self, s):
        """
        判断是否回文串
        """
        return s == s[::-1]


if __name__ == '__main__':
    a = Solution()
    print(a.validPalindrome("abca"))