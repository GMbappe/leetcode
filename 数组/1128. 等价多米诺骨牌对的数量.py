# _*_coding:utf-8 _*_
# @Time    : 2021/1/26 22:29
# @Author  : Guo 
# @File    : 1128. 等价多米诺骨牌对的数量.py
# @Desc    : https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/
"""
给你一个由一些多米诺骨牌组成的列表 dominoes。
如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。
形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。
在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。


示例：
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1
"""


class Solution:
    def numEquivDominoPairs(self, dominoes):
        # 二元数组计数  规定数组的第一个数字永远小于第二个
        # 然后计算数组的和， 然后计数
        res = 0
        num = [0] * 100
        for x, y in dominoes:
            a = x * 10 + y if x >= y else y * 10 + x
            res += num[a]
            num[a] += 1

        return res