# _*_coding:utf-8 _*_
# @Time    : 2022/4/11 21:06
# @Author  : Guo 
# @File    : 357. 统计各位数字都不同的数字个数.py
# @Desc    :

"""
给你一个整数 n ，统计并返回各位数字都不同的数字 x 的个数，其中 0 <= x < 10n 。
 
示例 1：
输入：n = 2
输出：91
解释：答案应为除去 11、22、33、44、55、66、77、88、99 外，在 0 ≤ x < 100 范围内的所有数字。

示例 2：
输入：n = 0
输出：1
"""


class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        n=0 1；n=1 10个 n=2 91个 可以是首位1-9之间 后位是0-9之间减1 9*9
        """
        if n == 0:
            return 1
        if n == 1:
            return 10
        cur = 9  # 首位可以有的数字
        res = 10
        for i in range(n - 1):
            cur *= 9 - i  # 相当于排列 9*A9 n-1  例如 2位数 9*A91=81+10
            res += cur
        return res