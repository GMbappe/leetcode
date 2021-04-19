# _*_coding:utf-8 _*_
# @Time    : 2021/1/10 10:03
# @Author  : Guo 
# @File    : 228. 汇总区间.py
# @Desc    : https://leetcode-cn.com/problems/summary-ranges/
"""
给定一个无重复元素的有序整数数组 nums 。
返回 恰好覆盖数组中所有数字 的 最小有序 区间范围列表。
也就是说，nums 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 nums 的数字 x 。
列表中的每个区间范围 [a,b] 应该按如下格式输出：
"a->b" ，如果 a != b
"a" ，如果 a == b
 

示例 1：
输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        每次比较下一个是否比当前大1，如果大一继续，否则单独成
        """
        if not nums:
            return []

        n = len(nums)
        res = []
        i = 0
        while i < n:
            left = nums[i]
            while i < n - 1 and (nums[i + 1] - nums[i]) == 1:
                i += 1
            right = nums[i]
            print(right)
            if left == right:
                res.append(str(left))
            else:
                res.append(str(left) + "->" + str(right))
            i += 1
            print(res)

        return res