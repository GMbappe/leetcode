# _*_coding:utf-8 _*_
# @Time    : 2020/12/11 23:32
# @Author  : Guo 
# @File    : 649. Dota2 参议院.py
# @Desc    : https://leetcode-cn.com/problems/dota2-senate/
"""

Dota2 的世界里有两个阵营：Radiant(天辉)和 Dire(夜魇)
Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的一项：
禁止一名参议员的权利：
参议员可以让另一位参议员在这一轮和随后的几轮中丧失所有的权利。
宣布胜利：如果参议员发现有权利投票的参议员都是同一个阵营的，他可以宣布胜利并决定在游戏中的有关变化。

给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了 Radiant（天辉）和 Dire（夜魇）。然后，如果有 n 个参议员，给定字符串的大小将是 n。
以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。
假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是 Radiant 或 Dire。

示例 2：
输入："RDD"
输出："Dire"
解释：
第一轮中,第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
第二个来自 Dire 阵营的参议员会被跳过因为他的权利被禁止
第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利
"""
from collections import deque


class Solution(object):
    def predictPartyVictory(self, senate):
        """
         贪心法则，
        首先将R和D 分别添加到两个队列里，
        当某一个队列为空时，则另外一方获胜
        依次比较R和D队列的首元素，那个小(因为序号小的级别高)，则另外的永久去掉，然后大的添加至队列末尾并将序号+n （n为整个元素长度；为了下次比较
        """
        n = len(senate)
        R = deque()
        D = deque()
        for k, v in enumerate(senate):
            if v == "R":
                R.append(k)
            else:
                D.append(k)

        while R and D:
            if R[0] < D[0]:
                R.append(R[0] + n)
            else:
                D.append(D[0] + n)
            R.popleft()
            D.popleft()

        return "Radiant" if R else "Dire"
