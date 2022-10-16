# _*_coding:utf-8 _*_
# @Time    : 2020/12/9 9:22
# @Author  : Guo 
# @File    : 62. 不同路径.py
# @Desc    : https://leetcode-cn.com/problems/unique-paths/
"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？

示例 1:
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        动态规划
        dp[m][n] = dp[m][n-1] + dp[m-1][n]  当前格子的路径数目等于他左边的路径和 + 上边的路径和
        """
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # 第一行 第一列 为 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[m - 1][n - 1]