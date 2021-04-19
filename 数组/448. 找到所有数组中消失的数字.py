# _*_coding:utf-8 _*_
# @Time    : 2021/2/13 11:12
# @Author  : Guo 
# @File    : 448. 找到所有数组中消失的数字.py
# @Desc    : https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
"""
给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
找到所有在 [1, n] 范围之间没有出现在数组中的数字。
您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。

示例:
输入:
[4,3,2,7,8,2,3,1]
输出:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        哈希表，然后分别计数，为0的key则为没有出现的
        """
        if not nums:
            return []
        a = dict()
        n = len(nums)
        for i in range(1, n + 1):
            a[i] = 0
        for j in nums:
            a[j] = a.get(j, 0) + 1

        res = []
        for x, y in a.items():
            if y == 0:
                res.append(x)
        return res
