# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 11:52
# @Author  : Guo 
# @File    : 11. 盛最多水的容器.py
# @Desc    : https://leetcode-cn.com/problems/container-with-most-water/
"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai)
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器。


示例 1：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针，
        如果left<= right 那么左指针向右移
        """
        left = 0
        right = len(height) - 1
        max_vol = 0
        while left < right:
            cur_vol = (right - left) * min(height[left], height[right])
            max_vol = max(max_vol, cur_vol)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_vol
