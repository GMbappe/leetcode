# _*_coding:utf-8 _*_
# @Time    : 2020/11/30 21:19
# @Author  : Guo 
# @File    : 767. 重构字符串.py
# @Desc    :

"""
给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
若可行，输出任意可行的结果。若不可行，返回空字符串

示例 1:
输入: S = "aab"
输出: "aba"

示例 2:
输入: S = "aaab"
输出: ""
"""

from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        """
        当n为奇数时候 如果某个字符出现的次数 大于 (n+1)/2 则 这个字母肯定会相邻
        当n为偶数时，如果某个字符出现次数 大于 n/2 则 这个字母肯定会相邻
        可以直接合并为 当某个字符出现次数大于(n+1)/2 则肯定会有重复
        贪心算法 基于最大堆的 将字母按照出现次数放入最大堆，
        首先将堆顶两个元素取出并合并，然后将剩余大于次数0的字符放入堆中，直到堆为空
        如果字符串为奇数时，每次取2个，一共n/2次，还剩一个字母，再次取出即可

        因为python自带时最小堆，所以字符计数需要带负号
        """
        n = len(S)

        if n < 2:  # 如果字符串长度较小，则直接返回
            return S

        char_counts = Counter(S)  # 统计字母出现次数  是个字典
        max_counts = max(set(char_counts.values()))
        if max_counts > (n + 1) // 2:
            return ""

        queue = [(-x[1], x[0]) for x in char_counts.items()]
        heapq.heapify(queue)
        ans = []

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)

            ans.extend([letter1, letter2])
            char_counts[letter1] -= 1
            char_counts[letter2] -= 1

            if char_counts[letter1] > 0:
                heapq.heappush(queue, (-char_counts[letter1], letter1))
            if char_counts[letter2] > 0:
                heapq.heappush(queue, (-char_counts[letter2], letter2))

        if queue:
            ans.extend(queue[0][1])

        return "".join(ans)