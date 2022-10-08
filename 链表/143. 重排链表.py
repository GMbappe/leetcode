# _*_coding:utf-8 _*_
# @Time    : 2022/9/26 11:59
# @Author  : Guo 
# @File    : 143. 重排链表.py
# @Desc    : https://leetcode.cn/problems/reorder-list/
"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：
L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


示例 1：

输入：head = [1,2,3,4]
输出：[1,4,2,3]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        mid = self.findMiddle(head)
        l1 = head
        l2 = mid.next
        mid.next = None
        l2 = self.reverseLink(l2)
        self.mergeLink(l1, l2)

    def findMiddle(self, head):
        """
        寻找中间节点
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseLink(self, head):
        """反转链表 """

        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre

    def mergeLink(self, l1, l2):
        # 合并链表
        while l1 and l2:
            l1_tmp = l1.next
            l2_tmp = l2.next

            l1.next = l2
            l1 = l1_tmp

            l2.next = l1
            l2 = l2_tmp





