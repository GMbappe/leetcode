# _*_coding:utf-8 _*_
# @Time    : 2022/5/7 17:17
# @Author  : Guo 
# @File    : 433. 最小基因变化.py
# @Desc    : BFS

"""
基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。
假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。
例如，"AACCGGTT" --> "AACCGGTA" 就是一次基因变化。
另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。
给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数
。如果无法完成此基因变化，返回 -1 。
注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。

示例 1：
输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
输出：1
"""
from collections import deque


class Solution:
    def minMutation(self, start, end, bank):
        """
        bfs
        """
        if start == end:
            return 0
        bank = set(bank)
        if end not in bank:
            return -1

        q = deque([(start, 0)])
        while q:
            s, cur_step = q.popleft()
            for i, x in enumerate(s):
                for y in 'ACGT':  # 尝试每一个字符的变换
                    if y != x:
                        cur_s = s[:i] + y + s[i + 1:]  # 进行拼接
                        if cur_s in bank:
                            if cur_s == end:  # 如果等于 则返回之前步骤+1
                                return cur_step + 1
                            bank.remove(cur_s)  # 已经得到这个字符不需要再次从这个字符串进行搜索
                            q.append((cur_s, cur_step + 1))

        return -1