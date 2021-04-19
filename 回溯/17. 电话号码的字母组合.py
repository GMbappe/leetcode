# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 15:17
# @Author  : Guo 
# @File    : 17. 电话号码的字母组合.py
# @Desc    : https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例 1：
输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""


class Solution:
    def letterCombinations(self, digits: str):
        """
        回溯：
        相当于先取第一个数字对应的可能字母，然后依次和接下来的数字对应的字母进行组合

        队列：
        初始化队列 queue = ['']
        取出第一个数字对应的字母，和之前队列的值合并然后放入队列中，
        然后再依次取出队列中的数据，再和接下来数字对应的字母合并，再放入，直到数字遍历结束
        """
        if not digits:
            return []

        self.mobile = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        self.stack = []
        self.combine("", digits)
        return self.stack

    def combine(self, letter, digits):
        if len(digits) == 0:
            self.stack.append(letter)
        else:
            for i in self.mobile[digits[0]]:
                self.combine(letter + i, digits[1:])
