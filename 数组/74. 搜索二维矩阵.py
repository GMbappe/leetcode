# _*_coding:utf-8 _*_
# @Time    : 2021/3/30 9:28
# @Author  : Guo 
# @File    : 74. 搜索二维矩阵.py
# @Desc    : https://leetcode-cn.com/problems/search-a-2d-matrix/
"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 
示例 1：
输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1
        while i < m and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:  # 说明数字在下面 行向下移动
                i += 1
            elif target < matrix[i][j]:  # 说明数字在左变 列向左移动
                j -= 1

        return False
