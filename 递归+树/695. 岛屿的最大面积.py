# _*_coding:utf-8 _*_
# @Time    : 2020/12/14 23:07
# @Author  : Guo 
# @File    : 695. 岛屿的最大面积.py
# @Desc    : https://leetcode-cn.com/problems/max-area-of-island/
"""
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1
"""


class Solution(object):
    def findMaxIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, self.bfs(grid, i, j, m, n))
        return res

    def bfs(self, grid, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
            return 0
        grid[i][j] = 2
        ans = 1
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ans += self.bfs(grid, i + x, j + y, m, n)

        return ans
