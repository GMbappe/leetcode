# _*_coding:utf-8 _*_
# @Time    : 2021/5/16 18:22
# @Author  : Guo 
# @File    : 148. 排序链表.py
# @Desc    : https://leetcode-cn.com/problems/sort-list/
"""
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head):
        """
        1. 找到链表中间节点，然后把链表分成两个子链表
          递归进行： 停止条件是 只剩一个节点
        2. 对子链表进行排序
        3. 合并子链表
        """
        if not head:
            return None
        return self.find_mid(head, None)

    def find_mid(self, head, tail):
        # 停止条件
        if head.next == tail:
            head.next = None
            return head
        slow, fast = head, head  # 设置快慢指针找中间节点，快指针每次两步，慢指针每次一步，快指针到头时，慢指针的位置就是中间节点
        while fast != tail:
            fast = fast.next
            slow = slow.next
            if fast != tail:  # 如果fast走一步后不是结尾，那么就再走一步，也就是每次走两步
                fast = fast.next
        mid = slow
        return self.merge(self.find_mid(head, mid), self.find_mid(mid, tail))  # 合并

    def merge(self, l1, l2):  # 合并链表
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
        # dummy_head = ListNode(0)
        # temp, temp1, temp2 = dummy_head, l1, l2
        # while temp1 and temp2: # 当两个链表都存在时候，开始比较大小
        #     if temp1.val < temp2.val:
        #         temp.next = temp1
        #         temp1 = temp1.next
        #     else:
        #         temp.next = temp2
        #         temp2 = temp2.next
        #     temp = temp.next

        # if temp1:
        #     temp.next = temp1
        # if temp2:
        #     temp.next = temp2
        # return dummy_head.next