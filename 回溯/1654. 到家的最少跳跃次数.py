# _*_coding:utf-8 _*_
# @Time    : 2022/8/18 18:26
# @Author  : Guo 
# @File    : 1654. 到家的最少跳跃次数.py
# @Desc    : https://leetcode.cn/problems/minimum-jumps-to-reach-home/
"""
1654. 到家的最少跳跃次数
有一只跳蚤的家在数轴上的位置 x 处。请你帮助它从位置 0 出发，到达它的家。

跳蚤跳跃的规则如下：

它可以 往前 跳恰好 a 个位置（即往右跳）。
它可以 往后 跳恰好 b 个位置（即往左跳）。
它不能 连续 往后跳 2 次。
它不能跳到任何 forbidden 数组中的位置。
跳蚤可以往前跳 超过 它的家的位置，但是它 不能跳到负整数 的位置。

给你一个整数数组 forbidden ，其中 forbidden[i] 是跳蚤不能跳到的位置，
同时给你整数 a， b 和 x ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 x 的可行方案，请你返回 -1 。


示例 1：
输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出：3
解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。

示例 2：
输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
输出：-1
"""

class Solution:
    def minimumJumps(self, forbidden, a, b, x):
        farest = max(max(forbidden)+a+b, x+b)
        forbid = set(forbidden)
        visit = set()
        step = 0
        stack = [[0, 0]]  # 当前达到的距离，以及是往前还是往后，用 1 和 -1 表示
        while stack:
            nxt = []
            for i, _ in stack:
                if i == x:
                    return step

            for i, d in stack:
                if i+a not in forbid and i+a <= farest and (i+a,1) not in visit:
                    nxt.append([i+a,1])
                    visit.add((i+a,1))
                if d != -1:
                    if i-b not in forbid and i-b >= 0 and (i-b,-1) not in visit:
                        nxt.append([i-b,-1])
                        visit.add((i-b,-1))
            step += 1
            stack = nxt
        return -1