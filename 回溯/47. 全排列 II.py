# _*_coding:utf-8 _*_
# @Time    : 2021/4/1 10:08
# @Author  : Guo 
# @File    : 47. 全排列 II.py
# @Desc    : https://leetcode-cn.com/problems/permutations-ii/

"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

示例 1：
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""


class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        self.stack = []
        n = len(nums)
        used = [False for _ in range(n)]
        self.back(0, [], nums, n, used)
        return self.stack

    def back(self, depth, path, nums, n, used):
        if depth == n:
            self.stack.append(path[:])
        for i in range(n):
            if not used[i]:
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:  # 必须剪掉，前一个相同的 并且前一个状态也是未使用
                    continue

                used[i] = True
                path.append(nums[i])
                self.back(depth+1, path, nums, n, used)
                used[i] = False
                path.pop()