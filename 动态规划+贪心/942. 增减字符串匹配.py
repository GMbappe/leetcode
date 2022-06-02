# _*_coding:utf-8 _*_
# @Time    : 2022/5/10 20:07
# @Author  : Guo 
# @File    : 942. 增减字符串匹配.py
# @Desc    :

"""
由范围 [0,n] 内所有整数组成的 n + 1 个整数的排列序列可以表示为长度为 n 的字符串 s ，其中:
如果 perm[i] < perm[i + 1] ，那么 s[i] == 'I' 
如果 perm[i] > perm[i + 1] ，那么 s[i] == 'D' 
给定一个字符串 s ，重构排列 perm 并返回它。如果有多个有效排列perm，则返回其中 任何一个 。

示例 1：
输入：s = "IDID"
输出：[0,4,1,3,2]

示例 2：
输入：s = "III"
输出：[0,1,2,3]
"""


class Solution:
    def diStringMatch(self, s):
        """
        贪心
        取得最大和最小值 顺序遍历 遇到 I 则选取当前最小的数，遇到D 则选取当前最大的数
        """
        n = len(s)
        max_num = n
        min_num = 0
        ans = [0] * (n+1)
        for i in range(n):
            if s[i] == 'I':
                ans[i] = min_num
                min_num += 1
            elif s[i] == 'D':
                ans[i] = max_num
                max_num -= 1
        ans[-1] = max_num
        return ans