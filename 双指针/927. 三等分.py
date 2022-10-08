# _*_coding:utf-8 _*_
# @Time    : 2022/10/6 14:20
# @Author  : Guo 
# @File    : 927. 三等分.py
# @Desc    : https://leetcode.cn/problems/three-equal-parts/
"""
给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。
如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
arr[0], arr[1], ..., arr[i] 为第一部分；
arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
这三个部分所表示的二进制值相等。
如果无法做到，就返回 [-1, -1]。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。
例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,1,1] 和 [1,1] 表示相同的值。


示例 1：
输入：arr = [1,0,1,0,1]
输出：[0,3]

示例 2：
输入：arr = [1,1,0,1,1]
输出：[-1,-1]

示例 3:
输入：arr = [1,1,0,0,1]
输出：[0,2]
"""


class Solution:
    def threeEqualParts(self, arr):
        """
        需要将1平均分为3等分
        首先找到每一部分第一个1所在的位置
        """
        s = sum(arr)
        if s % 3 != 0:  # 必须能够平分3等分
            return [-1, -1]
        if s == 0:  # 说明都是0
            return [0, 2]

        par = s // 3  # 每一份1的数量
        first = second = third = cur = 0  # 每个位置1的索引
        for i, num in enumerate(arr):  # 找到每一部分第一个1的索引
            if num == 1:
                if cur == 0:
                    first = i
                elif cur == par:
                    second = i
                elif cur == par * 2:
                    third = i
                cur += 1
        # 因为第三部分的数字是固定的，所以长度也是固定
        n = len(arr)
        length = n - third
        if first + length <= second and second + length <= third:
            i = 0
            # 第三部分开始向后移动，如果到最后也满足条件，则返回
            while third + i < n:
                if arr[first + i] != arr[second + i] or arr[first + i] != arr[third + i]:
                    return [-1, -1]
                i += 1
            return [first + length - 1, second + length]
        return [-1, -1]

