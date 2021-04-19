# _*_coding:utf-8 _*_
# @Time    : 2021/4/5 23:58
# @Author  : Guo 
# @File    : 79. 单词搜索.py
# @Desc    : https://leetcode-cn.com/problems/word-search/

"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。


示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        used = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.back(i, j, 0, board, word, used, m, n):
                    return True

        return False

    def back(self, i, j, p, board, word, used, m, n):
        if p == len(word) - 1:  # 终止条件
            return board[i][j] == word[p]
        if board[i][j] == word[p]:
            used[i][j] = True  # 改单词被使用
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and not used[x][y] and self.back(x, y, p + 1, board, word, used, m,
                                                                              n):  # 保证未被使用，且在范围内
                    return True
            used[i][j] = False  # 状态重置

        return False