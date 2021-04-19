# _*_coding:utf-8 _*_
# @Time    : 2020/12/15 1:05
# @Author  : Guo 
# @File    : 738. 单调递增的数字.py
# @Desc    : https://leetcode-cn.com/problems/monotone-increasing-digits/

"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。
（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:
输入: N = 10
输出: 9

示例 2:
输入: N = 1234
输出: 1234
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        贪心
        逆序 当遇到 i-1 大于 i时，i-1 要-1 然后 i到 n-1 变成 9
        """
        s = list(str(N))
        n = len(s)

        for i in range(n-1, 0, -1):
            if s[i-1] > s[i]:
                s[i-1] = str(int(s[i-1]) - 1)
                for j in range(i, n):
                    s[j] = "9"
        return int("".join(s))


if __name__ == '__main__':
    r = Solution()
    print(r.monotoneIncreasingDigits(332))