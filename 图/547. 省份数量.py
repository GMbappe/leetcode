# _*_coding:utf-8 _*_
# @Time    : 2021/1/8 0:01
# @Author  : Guo 
# @File    : 547. 省份数量.py
# @Desc    : https://leetcode-cn.com/problems/number-of-provinces/

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

 
示例 1：
输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
"""


class Solution:
    def findCircleNum(self, isConnected):
        """
        dfs
        1. 别分遍历有链接省就继续深度遍历，直到结束
        """

        def dfs(i):
            for j in range(provinces):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1
            else:
                continue

        return circles