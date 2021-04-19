# _*_coding:utf-8 _*_
# @Time    : 2021/3/29 15:41
# @Author  : Guo 
# @File    : 19. 删除链表的倒数第 N 个结点.py
# @Desc    : https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？

示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head: ListNode, n: int):
        """
        快慢指针， 快指针先做n步，
        然后每次一起向前走1步，当快指针到头时，慢指针对应位置就是倒数第n个点，跳过
        """
        if not head or n == 0:
            return head

        pre = ListNode()
        pre.next = head
        slow = pre
        fast = pre
        while n > 0:
            fast = fast.next
            n -= 1

        while fast.next:
            fast = fast.next
            low = low.next
        slow.next = slow.next.next

        return pre.next
