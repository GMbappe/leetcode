# _*_coding:utf-8 _*_
# @Time    : 2021/4/17 16:39
# @Author  : Guo 
# @File    : 220. 存在重复元素 III.py
# @Desc    :

"""
给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在两个下标 i 和 j，使得 abs(nums[i] - nums[j]) <= t ，同时又满足 abs(i - j) <= k 。
如果存在则返回 true，不存在返回 false。

示例 1：
输入：nums = [1,2,3,1], k = 3, t = 0
输出：true

示例 2：
输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
"""
from sortedcontainers import SortedList
import bisect


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t) -> bool:
        """
        使用一个「有序集合」去维护长度为 k 的滑动窗口内的数，该数据结构最好支持高效「查询」与「插入/删除」操作：
        查询：能够在「有序集合」中应用「二分查找」，快速找到「小于等于 uu 的最大值」和「大于等于 u 的最小值」（即「有序集合」中的最接近 u 的数）。
        插入/删除：在往「有序集合」添加或删除元素时，能够在低于线性的复杂度内完成（维持有序特性)。
        bisect_left函数是新元素会被放置于它相等的元素的前面，而 bisect_right返回的则是跟它相等的元素之后的位置
        """
        # O(N logk)
        window = SortedList()
        for i in range(len(nums)):
            # len(window) == k
            if i > k:  # 说明移动了
                window.remove(nums[i - 1 - k])
            window.add(nums[i])
            idx = bisect.bisect_left(window, nums[i])
            if idx > 0 and abs(window[idx] - window[idx - 1]) <= t:
                return True
            if idx < len(window) - 1 and abs(window[idx + 1] - window[idx]) <= t:
                return True
        return False
