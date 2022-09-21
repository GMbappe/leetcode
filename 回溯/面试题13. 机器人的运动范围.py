# _*_coding:utf-8 _*_
# @Time    : 2022/8/16 11:32
# @Author  : Guo 
# @File    : 面试题13. 机器人的运动范围.py
# @Desc    : https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/

"""
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 
示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
"""


class Solution:
    def movingCount(self, m, n, k):
        self.visited = set()
        self.dfs(m, n, k, 0, 0)
        return len(self.visited)

    def dfs(self, m, n, k, i, j):
        if i >= m or i < 0 or j < 0 or j >= n or (i, j) in self.visited or self.digit_sum(i) + self.digit_sum(
                j) > k:  # 如果不符合条件返回0
            return 0
        self.visited.add((i, j))  # 否则添加
        return 1 + self.dfs(m, n, k, i + 1, j) + self.dfs(m, n, k, i, j + 1)  # 方向只需要向右向下即可

    def digit_sum(self, num):
        res = 0
        while num != 0:
            res += num % 10
            num = num // 10
        return res