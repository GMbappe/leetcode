# _*_coding:utf-8 _*_
# @Time    : 2022/7/13 18:01
# @Author  : Guo 
# @File    : 735. 行星碰撞.py
# @Desc    : https://leetcode.cn/problems/asteroid-collision/
"""
给定一个整数数组 asteroids，表示在同一行的行星。
对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。
找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。
如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

示例 1：
输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。

示例 2：
输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。
"""


class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return []
        stack = []  # 辅助栈
        for i in asteroids:
            flag = True
            while flag and i < 0 and stack and stack[-1] > 0:  # 如果当前卫星小于0 则开始和辅助栈元素进行比较
                flag = stack[-1] < abs(i)
                if stack[-1] <= abs(i):
                    stack.pop()
            if flag:
                stack.append(i)

        return stack
