# _*_coding:utf-8 _*_
# @Time    : 2021/5/21 10:19
# @Author  : Guo 
# @File    : 围棋围起来的面积.py
# @Desc    :  阿里蚂蚁面试题目
"""
#   xxxxxx
#   xxxoxx
#   xxoxox
#   xxxoxx
#   xxxxxx

#output = 5

#   xxoxox
#   xxxoxx
#   xxxxxx
#   xxxxxx
#   xxxxxx

#   output=3

o 代表棋子
"""


def area(self, qipan):
    """
    用全部面积- 没有被围住的面积
    没有被围住面积：只需要从边缘开始DFS遍历即可 类似于求岛屿面积
    """
    m = len(qipan)
    n = len(qipan[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if (i in (0, m - 1) or j in (0, n - 1)) and qipan[i][j] == 'x':
                ans += self.dfs(qipan, i, j, m, n)
    res = m * n - ans
    return res


def dfs(self, qipan, i, j, m, n):
    if i < 0 or i >= m or j < 0 or j >= n or qipan[i][j] == 'o':
        return 0
    qipan[m][n] = 'o'
    ans = 1
    for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
        ans += self.bfs(qipan, x, y, m, n)
    return ans
