# _*_coding:utf-8 _*_
# @Time    : 2020/12/20 10:53
# @Author  : Guo 
# @File    : 316. 去除重复字母.py
# @Desc    : https://leetcode-cn.com/problems/remove-duplicate-letters/
"""
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）
示例 1：

输入：s = "bcabc"
输出："abc"
示例 2：

输入：s = "cbacdcbc"
输出："acdb"
"""

from collections import Counter


class Solution(object):
    def removeDuplicateLetters(self, s) -> str:
        """
        贪心+单调栈
        1. 遍历字符串， 对每个字符进行计数
        2. 创立单调栈，依次遍历字符串，如果栈为空则直接添加，如果栈里面存在该元素，则将计数-1，然后继续遍历，因为不能栈中不能有重复字符
           然后当栈不为空，比较当前字符和栈顶字符得大小，
           因为按照字典序，则需要栈顶元素最小，如果当前元素小于栈顶元素，则弹出栈顶元素，直到栈为空或者栈顶元素小于当前字符
           需要注意是，如果栈顶元素已经为0，则不能弹出
        """
        # count = dict()
        # for i in s:
        #     count[i] = count.get(i,0) + 1
        count = Counter(s)

        helper = []
        for i in s:
            if i in helper:
                count[i] -= 1
                continue
            while helper != [] and helper[-1] > i:
                if count[helper[-1]] == 0:
                    break
                helper.pop()
            helper.append(i)
            count[i] -= 1

        return "".join(helper)


if __name__ == '__main__':
    s = "cbacdcbc"
    res = Solution()
    print(res.removeDuplicateLetters(s))