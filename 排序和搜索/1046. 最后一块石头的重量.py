# _*_coding:utf-8 _*_
# @Time    : 2020/12/30 23:04
# @Author  : Guo 
# @File    : 1046. 最后一块石头的重量.py
# @Desc    : https://leetcode-cn.com/problems/last-stone-weight/
"""
有一堆石头，每块石头的重量都是正整数。
每一回合，从中选出两块 最重的 石头，然后将它们一起粉碎。假设石头的重量分别为 x 和 y，且 x <= y。那么粉碎的可能结果如下：
如果 x == y，那么两块石头都会被完全粉碎；
如果 x != y，那么重量为 x 的石头将会完全粉碎，而重量为 y 的石头新重量为 y-x。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 0。

示例：
输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
"""


class Solution:
    def lastStoneWeight(self, stones):
        """
        倒序排序，
        建立索引，依次比较如果两个相同，则都弹出，否则只弹出
        """
        if not stones:
            return 0

        n = len(stones)
        while n > 1 and stones:
            stones.sort(reverse=True)
            a = stones.pop(0)
            b = stones.pop(0)
            if a == b:
                n = len(stones)
                continue
            else:
                stones.append(abs(a - b))
                n = len(stones)
        if n == 1:
            return stones[0]
        if n == 0:
            return 0