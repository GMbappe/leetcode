# _*_coding:utf-8 _*_
# @Time    : 2021/3/27 11:57
# @Author  : Guo 
# @File    : 61. 旋转链表.py
# @Desc    : https://leetcode-cn.com/problems/rotate-list/

"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def rotateRight(self, head, k):
        """
        1. 求链表长度 n
        2. 双指针 快慢指针， 快指针比慢指针先走k步，然后共同走，当快指针走到某位时，慢指针的对象即为新链表的某位，下一位时头指针
        3. 重构链表， 慢指针下一位时新链表头，快指针的下一位链接到原指针的头节点，慢指针某位指向空
        :param head:
        :param k:
        :return: ListNode
        """
        if not head or k == 0:
            return head

        n = 1
        cur = head  # 创建当前节点
        while cur.next:  # 计算长度
            cur = cur.next
            n += 1

        k = k % n  # k除长度取余，
        if k == 0:
            return head

        slow = head
        fast = head
        while k > 0:  # 先让快指针走k步
            fast = fast.next
            k -= 1

        while fast.next:  # 共同走 直到快指针到原链表尾节点
            slow = slow.next
            fast = fast.next

        new_head = slow.next  # 开启新链表头节点，为慢指针下一个
        slow.next = None  # 慢指针后为空
        fast.next = head  # 快指针指向头节点

        return new_head