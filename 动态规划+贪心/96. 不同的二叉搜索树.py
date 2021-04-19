# _*_coding:utf-8 _*_
# @Time    : 2021/4/12 23:49
# @Author  : Guo 
# @File    : 96. 不同的二叉搜索树.py
# @Desc    :https://leetcode-cn.com/problems/unique-binary-search-trees/

"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
"""


class Solution:
    def numTrees(self, n) -> int:
        """
        建以3为根、长度为7的不同二叉搜索树，
        整个序列是[1,2,3,4,5,6,7]，我们需要从左子序列[1,2] 构建左子树，
        从右子序列[4,5,6,7] 构建右子树，然后将它们组合（即笛卡尔积）
        所以如果n=7则需要遍历每个点当作根节点，然后把所有组合求和
        dp[i] += dp[i-1]（左边节点数）* dp[i-j]（右边节点数）
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]

        return dp[n]