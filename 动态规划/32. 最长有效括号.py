# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 23:49
# @Author  : Guo 
# @File    : 32. 最长有效括号.py
# @Desc    : https://leetcode-cn.com/problems/longest-valid-parentheses/

"""
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。

示例 1：
输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

示例 2：
输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"
"""


class Solution:
    def longestValidParentheses(self, s: str):
        """
        dp[i]  表示以i索引结尾的最长连续字串数目
        if s[i] = "(" 则 dp[i] = 0  因为不可能右以左括号结尾且成对的
        if s[i] = ")"  形如 “))”  此时 i > 0
            if s[i-1] = ")" 且 s[i-dp[i-1]-1] = "(" 则表明找到结对的地方，需要再加上之前位置的括号数目
                dp[i] = dp[i-1] +2 + dp[i-dp[i-1]-2]
            if s[i-1] = "("  形如 “()”
                dp[i] = dp[i-2] + 2
        """
        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        for i in range(n):
            if i > 0 and s[i] == ")":  # 不能以) 开头
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
        return max(dp)


if __name__ == '__main__':
    s = "(()())"
    a = Solution()
    print(a.longestValidParentheses(s))