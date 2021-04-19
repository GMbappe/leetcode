# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 18:43
# @Author  : Guo 
# @File    : 23. 合并K个升序链表.py
# @Desc    : https://leetcode-cn.com/problems/merge-k-sorted-lists/

"""
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, l, r):
        if l > r:
            return
        if l == r:
            return lists[l]

        mid = (l + r) // 2
        l1 = self.merge(lists, l, mid)
        l2 = self.merge(lists, mid + 1, r)
        return self.mergeTwo(l1, l2)

    def mergeTwo(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwo(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwo(l1, l2.next)
            return l2