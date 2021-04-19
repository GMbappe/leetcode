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
        """
        核心 当前位置能填充的雨水 = min(左边最大高度， 右边最大高度) - 当前位置高度
        算出来每一个位置的雨水量 然后 求和
        :param height:
        :return:
        """
        if not height:
            return 0
        n = len(height)
        l = 0
        r = n - 1
        l_max = 0
        r_max = 0
        ans = 0
        while l < r:
            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])
            if l_max < r_max:
                h = l_max - height[l]
                ans += h
                l += 1
            else:
                h = r_max - height[r]
                ans += h
                r -= 1

        return ans
