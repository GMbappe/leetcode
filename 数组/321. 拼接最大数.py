# _*_coding:utf-8 _*_
# @Time    : 2020/12/2 9:06
# @Author  : Guo 
# @File    : 321. 拼接最大数.py
# @Desc    :
"""
给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。
现在从这两个数组中选出 k (k <= m + n) 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。
求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。
说明: 请尽可能地优化你算法的时间和空间复杂度

示例 1:
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]

示例 2:
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
"""
"""
1. 首先将两个数组拆成最大子序列 x,y 满足 x+y = k
2. 自定义方法 合并两个子序列
3. 比较每次合并的子序列数
两个子序列的长度最小为0，最大不能超过k 且不能超过对应的数组长度
"""


class Solution:
    def maxNumber(self, nums1, nums2, k):
        m = len(nums1)
        n = len(nums2)
        maxNumber = [0] * k  # 返回的最大数
        for i in range(k + 1):
            len_2 = k - i
            if i <= m and k - i <= n:
                sequence1 = self.getMaxSequence(nums1, i)
                sequence2 = self.getMaxSequence(nums2, k - i)
                max_sequence = self.mergeSequence(sequence1, sequence2, k)
                if maxNumber < max_sequence:
                    maxNumber = max_sequence

        return maxNumber

    def getMaxSequence(self, nums, k):
        # 取含k个元素的最大子序列
        if k == 0:
            return []

        stack = []
        remain = len(nums) - k  # 表示还剩几个元素
        for num in nums:
            while remain != 0 and stack != [] and stack[-1] < num:
                remain -= 1
                stack.pop()
            stack.append(num)
        return stack[:k]

    def mergeSequence(self, nums1, nums2, k):
        res = []
        for i in range(k):
            res.append(max(nums1, nums2).pop(0))
        return res


if __name__ == '__main__':
    a = [1, 2, 3]
    print("".join(str(i) for i in a))

