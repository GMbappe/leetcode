# _*_coding:utf-8 _*_
# @Time    : 2021/6/6 20:53
# @Author  : Guo 
# @File    : 474. 一和零.py
# @Desc    : https://leetcode-cn.com/problems/ones-and-zeroes/
"""
给你一个二进制字符串数组 strs 和两个整数 m 和 n 。
请你找出并返回 strs 的最大子集的大小，该子集中 最多 有 m 个 0 和 n 个 1 。
如果 x 的所有元素也是 y 的元素，集合 x 是集合 y 的 子集 。


示例 1：
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。
"""


class Solution:
    def findMaxForm(self, strs, m, n) -> int:
        """
        dp[i][m][n]  到第i子符时，满足至多m个0和n个1的最大集合数
        dp[i][m][n] = dp[i-1][m-这个字符0个数][n-这个字符1个数] + 1 或者 不选这个字符
        空间优化 dp[m][n] 逆序求，因为每次的结果只和上一层有关系，所以必须要逆序求，先用上一层最大的，然后再计算
        """
        # j = len(strs)
        # dp = [[[0 for _ in range(n+1)] for _ in range(m+1)] for _ in range(j+1)]

        # for i in range(1, j+1):
        #     cur = self.count(strs[i-1])  # 选取当前字符串 0 1 个数
        #     for p in range(0, m+1):
        #         for q in range(0, n+1):
        #             dp[i][p][q] = dp[i-1][p][q]
        #             zeros = cur[0]
        #             ones = cur[1]
        #             if p >= zeros and q >= ones:
        #                 dp[i][p][q] = max(dp[i-1][p][q], dp[i-1][p-zeros][q-ones]+1)
        # return dp[j][m][n]
        j = len(strs)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in strs:
            cur = self.count(i)
            zeros = cur[0]
            ones = cur[1]
            for p in range(m, zeros - 1, -1):
                for q in range(n, ones - 1, -1):
                    dp[p][q] = max(dp[p][q], dp[p - zeros][q - ones] + 1)
        return dp[m][n]

    def count(self, strs):
        res = [0] * 2
        for i in strs:
            if i == "0":
                res[0] += 1
            elif i == "1":
                res[1] += 1
        return res