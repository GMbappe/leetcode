# _*_coding:utf-8 _*_
# @Time    : 2022/8/15 13:03
# @Author  : Guo 
# @File    : 剑指 Offer 21. 调整数组顺序使奇数位于偶数前面.py
# @Desc    : https://leetcode.cn/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数在数组的前半部分，所有偶数在数组的后半部分。

示例：
输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。
"""
class Solution:
    def exchange(self, nums):
        """
        双指针
        如果左指针的数字是奇数则跳过
        如果右指针数字是偶数则跳过
        否则交换位置
        """
        n = len(nums)
        i = 0
        j = n-1
        while i<j:
            if i<j and nums[i]%2==1:
                i+=1
            if i<j and nums[j]%2==0:
                j -= 1
            nums[i],nums[j] = nums[j], nums[i]
        return nums