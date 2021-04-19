# _*_coding:utf-8 _*_
# @Time    : 2021/3/25 22:57
# @Author  : Guo 
# @File    : 82. 删除排序链表中的重复元素 II.py
# @Desc    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        创造哑节点p 以及当前节点cur 指向p, 每次移动当前节点，最后返回p.next
        :param head: ListNode
        :return: Listnode
        """
        if not head:
            return head
        p = ListNode(0)
        p.next = head
        cur = p
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return p.next

