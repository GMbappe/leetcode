# _*_coding:utf-8 _*_
# @Time    : 2020/12/7 23:51
# @Author  : Guo 
# @File    : 861. 翻转矩阵后的得分.py
# @Desc    : https://leetcode-cn.com/problems/score-after-flipping-matrix/

"""
有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
返回尽可能高的分数。

示例：
输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
"""


class Solution(object):
    def matrixScore(self, A):
        """
        1. 将所有第一列的数字全部变为1, 如果不为1，则转换行
        2. 从第二列开始 如果当前列1的数目小于0的数目，则反转
        3. 计算结果
        """
        m = len(A)
        n = len(A[0])

        for i in range(m):
            if A[i][0] == 0:
                # 翻转所在行
                for j in range(n):
                    A[i][j] = 1 - A[i][j]

        # 统计列中1和0的个数
        for j in range(1, n):
            count0 = 0
            count1 = 0
            for i in range(m):
                if A[i][j] == 0:
                    count0 += 1
                elif A[i][j] == 1:
                    count1 += 1
            if count0 > count1:
                for i in range(m):
                    A[i][j] = 1 - A[i][j]
        # 开始算数
        res = 0
        for i in range(m):
            temp = ""
            for j in range(n):
                temp += str(A[i][j])
            res += int(temp, 2)
        return res
