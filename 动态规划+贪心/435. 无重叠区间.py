# _*_coding:utf-8 _*_
# @Time    : 2020/12/31 10:08
# @Author  : Guo 
# @File    : 435. 无重叠区间.py
# @Desc    : https://leetcode-cn.com/problems/non-overlapping-intervals/
"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
"""


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        1. 按照右边界排序
        2. 开始比较，如果遇到右边界 小于等于 下个区间的左边界， 则不用删除，然后更新右边界
                    如果遇到右边界大于 左边界，则计数 + 1
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        right = intervals[0][1]  # 初始化 右边界
        res = 0
        for i in range(1, n):
            if right <= intervals[i][0]:
                right = intervals[i][1]
            else:
                res += 1
        return res
