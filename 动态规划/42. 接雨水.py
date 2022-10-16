# _*_coding:utf-8 _*_
# @Time    : 2021/4/2 21:03
# @Author  : Guo 
# @File    : 42. 接雨水.py
# @Desc    : https://leetcode-cn.com/problems/trapping-rain-water/

"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
"""


class Solution:
    def trap(self, height):
        if not height:
            return 0
        n = len(height)
        l_max = [height[0]] + [0] * (n - 1)
        r_max = [0] * (n - 1) + [height[n - 1]]

        for i in range(1, n):  # 寻找每个索引位置及其左边做大高度
            l_max[i] = max(l_max[i - 1], height[i])

        for i in range(n - 2, -1, -1):  # 寻找每个索引位置及其右边最大高度
            r_max[i] = max(r_max[i + 1], height[i])

        return sum([min(l_max[i], r_max[i]) - height[i] for i in range(n)])