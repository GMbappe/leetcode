# _*_coding:utf-8 _*_
# @Time    : 2021/5/27 0:06
# @Author  : Guo 
# @File    : 221. 最大正方形.py
# @Desc    : https://leetcode-cn.com/problems/maximal-square/
"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
"""


class Solution:
    def maximalSquare(self, matrix):
        """
        dp
        dp[i][j] 代表以第几行第几列为右下角的正方形的最大边长
        分别是左上角，上面，左边的最小值 + 1
        dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        """
        if not matrix:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        maxSquare = maxSide * maxSide
        return maxSquare

