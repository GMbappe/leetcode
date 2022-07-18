# _*_coding:utf-8 _*_
# @Time    : 2022/6/27 18:07
# @Author  : Guo 
# @File    : 522. 最长特殊序列 II.py
# @Desc    : https://leetcode.cn/problems/longest-uncommon-subsequence-ii/

"""
给定字符串列表 strs ，返回其中 最长的特殊序列 。如果最长特殊序列不存在，返回 -1 。
特殊序列 定义如下：该序列为某字符串 独有的子序列（即不能是其他字符串的子序列）。
 s 的 子序列可以通过删去字符串 s 中的某些字符实现。
例如，"abc" 是 "aebdc" 的子序列，因为您可以删除"aebdc"中的下划线字符来得到 "abc" 。"aebdc"的子序列还包括"aebdc"、 "aeb" 和 "" (空字符串)。


示例 1：
输入: strs = ["aba","cdc","eae"]
输出: 3
"""
class Solution:
    def findLUSlength(self, strs):
        """
        寻找特殊字符串 就是寻找不是其他字符串字串的
        判断是否i 是否是 j的字串，双指针，
        """
        # strs = strs.sort(key= lambda x:len(x))
        n = len(strs)
        ans = -1
        for i in range(n):
            check = True
            for j in range(n):
                if i != j and self.judgeStr(strs[i], strs[j]):
                    check = False
                    break
            if check:
                ans = max(len(strs[i]), ans)
        return ans

    def judgeStr(self, s1, s2):
        i = 0
        j = 0
        m = len(s1)
        n = len(s2)
        while i<m and j < n:
            if s1[i] == s2[j]:
                i += 1
                j += 1
            else:
                j += 1
        return i==m