# _*_coding:utf-8 _*_
# @Time    : 2021/1/5 23:08
# @Author  : Guo 
# @File    : 830. 较大分组的位置.py
# @Desc    : https://leetcode-cn.com/problems/positions-of-large-groups/
"""
在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。
例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。
分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。
我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
找到每一个 较大分组 的区间，按起始位置下标递增顺序排序后，返回结果。


示例 1：
输入：s = "abbxxxxzzy"
输出：[[3,6]]
解释："xxxx" 是一个起始于 3 且终止于 6 的较大分组。
"""


class Solution:
    def largeGroupPositions(self, s):
        """
        顺序遍历 
        """
        if not s:
            return []

        res = []
        i = 0
        n = len(s)
        while i < n - 1:
            count = 1
            j = i
            while j < n - 1 and s[j] == s[j + 1]:
                count += 1
                j += 1
            if count >= 3:
                res.append([i, i + count - 1])
            if count > 0:
                i += count
            else:
                i += 1

        return res