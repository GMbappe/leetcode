# _*_coding:utf-8 _*_
# @Time    : 2021/2/28 20:15
# @Author  : Guo 
# @File    : 896. 单调数列.py
# @Desc    : https://leetcode-cn.com/problems/monotonic-array/
"""
如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。 如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。


示例 1：
输入：[1,2,2,3]
输出：true

示例 2：
输入：[6,5,4,4]
输出：true
"""


class Solution:
    def isMonotonic(self, A) -> bool:
        """
        1. 两个布尔型判断 数列是单调增 还是单调减
        2. 顺序遍历，最后判断两个布尔型是否相同
        """
        n = len(A)
        sx = True  # 顺序
        nx = True  # 逆序
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                sx = False
            if A[i] < A[i + 1]:
                nx = False
        return nx or sx
