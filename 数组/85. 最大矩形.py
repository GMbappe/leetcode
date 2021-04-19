# _*_coding:utf-8 _*_
# @Time    : 2020/12/27 0:19
# @Author  : Guo 
# @File    : 85. 最大矩形.py
# @Desc    : https://leetcode-cn.com/problems/maximal-rectangle/
"""
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

示例 1：
输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
"""


class Solution:
    def maximalRectangle(self, matrix):
        """
        1. 遍历矩阵 生成 left[i][j] 表示 第i行第j列的从左边到该位置的连续1的数量
           left[i][j] = left[i][j-1] + 1 if matrix[i][j] = 1
                      = 0  if matrix[i][j] != 1
        2. 然后遍历left矩阵， 如果遇到1，则开始计算以该格子为矩形右下角的最大面积，依次想上开始，矩阵的宽就是该列的最小值left[k][j]  0<=k<=i , 高是 每次+1
        """
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        helper = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if j > 0:
                        helper[i][j] = helper[i][j - 1] + 1
                    else:
                        helper[i][j] = 1
                else:
                    helper[i][j] = 0

        res = 0  # 返回最大矩阵
        for i in range(m):
            for j in range(n):
                if helper[i][j] == 0:
                    continue
                width = helper[i][j]  # 当前单元格的宽 也就是1的数量
                area = 1 * helper[i][j]  # 区域面积
                count = 2
                k = i - 1
                while k >= 0:
                    if helper[k][j] == 0:
                        break
                    else:
                        width = min(width, helper[k][j])
                        area = max(width * count, area)
                    count += 1
                    k -= 1
                res = max(res, area)
        return res