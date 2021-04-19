# _*_coding:utf-8 _*_
# @Time    : 2021/4/12 9:58
# @Author  : Guo 
# @File    : 179. 最大数.py
# @Desc    : https://leetcode-cn.com/problems/largest-number/

"""
给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。
注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

示例 1：
输入：nums = [10,2]
输出："210"

示例 2：
输入：nums = [3,30,34,5,9]
输出："9534330"
"""

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums) -> str:
        nums.sort(key=cmp_to_key(self.compare), reverse=True)
        return str(int("".join(str(s) for s in nums)))

    def compare(self, x, y):
        """
        比较换位之后那个大，如果更大则在前面
        """
        if int(str(x) + str(y)) > int(str(y) + str(x)):
            return 1
        elif int(str(x) + str(y)) < int(str(y) + str(x)):
            return -1
        else:
            return 0