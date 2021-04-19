# _*_coding:utf-8 _*_
# @Time    : 2020/12/14 10:04
# @Author  : Guo 
# @File    : 49. 字母异位词分组.py
# @Desc    : https://leetcode-cn.com/problems/group-anagrams/
"""
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:
输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        使用字典，key为字符串得顺序排列
        最后返回值
        """
        res = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in res:
                res[key] = [s]  # 结果变成列表 
            else:
                res[key].append(s)
        return list(res.values())
