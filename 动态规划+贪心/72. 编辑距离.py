# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 21:15
# @Author  : Guo 
# @File    : 72. 编辑距离.py
# @Desc    : https://leetcode-cn.com/problems/edit-distance/

"""
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
 
示例 1：
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        动态规划
        dp[i][j]  表示word1的[:i]字符和word2[:j]的最少编辑距离
        dp[i][j] =min(dp[i-1][j]+1, dp[i][j-1]+1,dp[i-1][j-1])  # 如果w1[i] = w[j]
                = min(dp[i-1][j]+1, dp[i][j-1]+1,dp[i-1][j-1]+1)  否则
        dp[0][j] = j
        dp[i][0] = i
        """
        m = len(word1)
        n = len(word2)

        if m * n == 0:
            return m + n

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i

        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 1)

        return dp[m][n]
