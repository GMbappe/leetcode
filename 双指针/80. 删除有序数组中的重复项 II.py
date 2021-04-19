# _*_coding:utf-8 _*_
# @Time    : 2021/4/6 0:20
# @Author  : Guo 
# @File    : 80. 删除有序数组中的重复项 II.py
# @Desc    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/

"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

 
示例 1：
输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

示例 2：
输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。
"""


class Solution:
    def removeDuplicates(self, nums) -> int:
        """
        快慢指针，slow fast
        slow指针代表待置换处的索引，如果fast和代置换后面两数字一样，
        则说明存在重复元素，fast向前移动，直到和元素不相同，然后置换，同时slow指针和fast一起向前移动
        """
        n = len(nums)
        if n <= 2:
            return n

        slow = 2  # 代表要置换的元素
        for i in range(2, n):
            if nums[i] != nums[slow - 2]:
                nums[slow] = nums[i]
                slow += 1
        return slow