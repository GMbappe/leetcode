# _*_coding:utf-8 _*_
# @Time    : 2020/12/12 23:12
# @Author  : Guo 
# @File    : 376. 摆动序列.py
# @Desc    : https://leetcode-cn.com/problems/wiggle-subsequence/
"""
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为摆动序列。第一个差（如果存在的话）可能是正数或负数。少于两个元素的序列也是摆动序列。
例如， [1,7,4,9,2,5] 是一个摆动序列，因为差值 (6,-3,5,-7,3) 是正负交替出现的。
相反, [1,4,7,2,5] 和 [1,7,4,5,5] 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
给定一个整数序列，返回作为摆动序列的最长子序列的长度。 通过从原始序列中删除一些（也可以不删除）元素来获得子序列，剩下的元素保持其原始顺序

示例 1:
输入: [1,7,4,9,2,5]
输出: 6
解释: 整个序列均为摆动序列。

示例 2:
输入: [1,17,5,10,13,15,10,5,16,8]
输出: 7
解释: 这个序列包含几个长度为 7 摆动序列，其中一个可为[1,17,10,13,10,16,8]
"""


class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        DP
        分别设置 上升摇摆序列队列(最后一个数大于前一个数)  下降摇摆序列队列(最后一个数小于前一个数)
        如果相同 则 跳过 继续比较
        up[i] =  up[i-1]   when nums[i] <= nums[i-1]
              = max(up[i-1], down[i-1]+1)  when nums[i] > nums[i-1]
        """
        n = len(nums)
        if n < 2:
            return n

        up = [1] * n
        down = [1] * n

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(down[i - 1], up[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])