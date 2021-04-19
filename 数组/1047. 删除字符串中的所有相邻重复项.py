# _*_coding:utf-8 _*_
# @Time    : 2021/3/9 22:12
# @Author  : Guo 
# @File    : 1047. 删除字符串中的所有相邻重复项.py
# @Desc    : https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/

"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。
在 S 上反复执行重复项删除操作，直到无法继续删除。
在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

示例：
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。
之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。
"""


class Solution:
    def removeDuplicates(self, S):
        """
        辅助栈
        1. 当辅助栈为空时候，入栈，
        2. 不为空时候，进行判断，如果栈顶元素和出栈元素一致时，则一起都弹出去，
           否则 元素入栈
        """
        if not S:
            return ""
        stack = []
        for s in S:
            if stack and stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)

        return ''.join(stack)
