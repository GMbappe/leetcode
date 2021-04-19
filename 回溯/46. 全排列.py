# _*_coding:utf-8 _*_
# @Time    : 2021/4/1 0:37
# @Author  : Guo 
# @File    : 46. 全排列.py
# @Desc    : https://leetcode-cn.com/problems/permutations/

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        self.res = []
        n = len(nums)
        used = [False for _ in range(n)]
        self.back(0, [], nums, n, used)
        return self.res

    def back(self, depth, path, nums, n, used):
        if depth == n:  # 当达到停止条件时 添加
            self.res.append(path[:])
        for i in range(n):
            if not used[i]:  # 当数字还未被使用
                used[i] = True  # 已经被使用
                path.append(nums[i])
                self.back(depth + 1, path, nums, n, used)  # 一定是depth+1
                used[i] = False  # 状态重置
                path.pop()  # 撤销
