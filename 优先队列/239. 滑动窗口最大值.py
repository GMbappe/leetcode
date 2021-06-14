# _*_coding:utf-8 _*_
# @Time    : 2021/6/14 19:19
# @Author  : Guo 
# @File    : 239. 滑动窗口最大值.py
# @Desc    : https://leetcode-cn.com/problems/sliding-window-maximum/

"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。

示例 1：
输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""
import heapq


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        1. 使用堆，堆大小为k 每个数字和索引在一起
        2. 因为是最小堆，就是可以使用 (-nums[i],i)
        3. 排在最上面的就是当前窗口最大值，但是这个值的索引不一定在窗口范围内，如果不在范围内则弹出
        """
        n = len(nums)
        if k > n:
            return max(nums)
        q = [(-nums[i], i) for i in range(k)]  # 创造大小为k的堆
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans