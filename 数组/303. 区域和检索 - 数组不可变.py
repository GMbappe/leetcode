# _*_coding:utf-8 _*_
# @Time    : 2021/3/1 16:42
# @Author  : Guo 
# @File    : 303. 区域和检索 - 数组不可变.py
# @Desc    : https://leetcode-cn.com/problems/range-sum-query-immutable/
"""
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。
实现 NumArray 类：
NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
 

示例：
输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]
解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1))
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
"""


class NumArray:
    """
    利用前缀和  s[j+1] - s[i] 表示索引 i到j的和
    """

    def __init__(self, nums):
        n = len(nums)
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]
