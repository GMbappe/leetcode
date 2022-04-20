# _*_coding:utf-8 _*_
# @Time    : 2022/4/9 18:05
# @Author  : Guo 
# @File    : 780. 到达终点.py
# @Desc    :

"""
给定四个整数 sx , sy ，tx 和 ty，如果通过一系列的转换可以从起点 (sx, sy) 到达终点 (tx, ty)，则返回 true，否则返回 false。
从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。


示例 1:
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

示例 2:
输入: sx = 1, sy = 1, tx = 2, ty = 2
输出: false
"""


class Solution:
    def reachingPoints(self, x, y, tx, ty) -> bool:
        return self.dfs(x, y, tx, ty)

    def dfs(self, x, y, tx, ty):
        """
        从终点开始，如果从起点开始则可能情况较多，容易超时；
        """
        if x > tx or y > ty:
            return False
        if x == tx:  # 如果横坐标相同，则比较纵坐标之差能否整除横坐标
            return ((ty - y) % x) == 0
        elif y == ty:
            return ((tx - x) % y) == 0

        if tx < ty:  # 先处理值大的终点坐标 例如 (3,10) 肯定是通过不断加3得到的 基坐标是(3,1)
            return self.dfs(x, y, tx, ty % tx)
        else:
            return self.dfs(x, y, tx % ty, ty)