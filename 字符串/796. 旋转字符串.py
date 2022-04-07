# _*_coding:utf-8 _*_
# @Time    : 2022/4/7 21:22
# @Author  : Guo 
# @File    : 796. 旋转字符串.py
# @Desc    :
"""
给定两个字符串, s 和 goal。如果在若干次旋转操作之后，s 能变成 goal ，那么返回 true 。
s 的 旋转操作 就是将 s 最左边的字符移动到最右边。 
例如, 若 s = 'abcde'，在旋转一次之后结果就是'bcdea' 。

示例 1:
输入: s = "abcde", goal = "cdeab"
输出: true

示例 2:
输入: s = "abcde", goal = "abced"
输出: false
"""


class Solution(object):
    def rotateString(self, s, goal):
        n = len(s)
        m = len(goal)
        if m != n:
            return False
        # n次循环，每次旋转一次，然后比较
        for _ in range(n + 1):
            print(s)
            if s == goal:
                return True
            s = s[1:] + s[0]
        return False
