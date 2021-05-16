# _*_coding:utf-8 _*_
# @Time    : 2021/5/16 22:27
# @Author  : Guo 
# @File    : 206. 反转链表.py
# @Desc    : https://leetcode-cn.com/problems/reverse-linked-list/
"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        1. 创建临时空节点, 当前节点
        2. 每次当前节点移动后，当前节点指向下一节点，然后当前节点的下一节点指向pre节点，然后pre移动，当前节点移动
        """
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        return pre