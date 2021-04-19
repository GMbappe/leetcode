# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 18:02
# @Author  : Guo 
# @File    : 64. 最小路径和.py
# @Desc    : https://leetcode-cn.com/problems/minimum-path-sum/


"""
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例 1：
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        dp[m][n] = min(dp[m-1][n], dp[m][n-1])  选择左边或者上面最小的
        # 如果是第一行或者第一列，只能是加左边或者上边
        """
        if not grid:
            return 0

        dp = grid
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j > 0:  # 第一行
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0 and i > 0:  # 第一列
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]