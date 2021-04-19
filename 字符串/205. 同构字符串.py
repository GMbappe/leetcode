# _*_coding:utf-8 _*_
# @Time    : 2020/12/27 20:25
# @Author  : Guo 
# @File    : 205. 同构字符串.py
# @Desc    : https://leetcode-cn.com/problems/isomorphic-strings/
"""
给定两个字符串 s 和 t，判断它们是否是同构的。
如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

示例 1:
输入: s = "egg", t = "add"
输出: true
"""


class Solution:
    def isIsomorphic(self, s, t) -> bool:
        """
        建立两个hashmap进行互射
        然后依次比较
        """
        s_dic = dict()
        t_dic = dict()

        for x, y in zip(s, t):
            if (x in s_dic and s_dic[x] != y) or (y in t_dic and t_dic[y] != x):
                return False
            s_dic[x] = y
            t_dic[y] = x
        return True
