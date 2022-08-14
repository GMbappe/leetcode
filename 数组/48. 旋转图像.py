# _*_coding:utf-8 _*_
# @Time    : 2020/12/19 12:09
# @Author  : Guo 
# @File    : 48. 旋转图像.py
# @Desc    : https://leetcode-cn.com/problems/rotate-image/
"""
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""


class Solution(object):
    def rotate_image(self, matrix):
        """
        先转置矩阵，然后再每一行反转
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i, n):  # 保持已经变换过的 不动
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(m):
            matrix[i] = matrix[i][::-1]

        return matrix

    def reverse_rotate_image(self, matrix):
        """
        逆时针旋转图像
        """
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(0,n-i):  # 保持已经变换过的 不动
                matrix[i][j], matrix[n-j-1][n-i-1] = matrix[n-j-1][n-i-1], matrix[i][j]
        for i in range(m):
            matrix[i] = matrix[i][::-1]

        return matrix
