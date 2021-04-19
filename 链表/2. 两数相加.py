# _*_coding:utf-8 _*_
# @Time    : 2021/3/27 22:52
# @Author  : Guo 
# @File    : 2. 两数相加.py
# @Desc    : https://leetcode-cn.com/problems/add-two-numbers/

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0  # 表示是否进位
        a1 = 0
        a2 = 0
        head = ListNode(0)
        cur = head
        while l1 or l2:  # 如果不存在就当作0
            if l1:
                a1 = l1.val
            else:
                a1 = 0
            if l2:
                a2 = l2.val
            else:
                a2 = 0

            s = a1 + a2 + flag
            cur.next = ListNode(s % 10)
            cur = cur.next
            flag = s // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if flag == 1:
            cur.next = ListNode(flag)
        return head.next