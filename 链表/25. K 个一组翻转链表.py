# _*_coding:utf-8 _*_
# @Time    : 2021/4/21 10:17
# @Author  : Guo 
# @File    : 25. K 个一组翻转链表.py
# @Desc    : https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
 
示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        pre 下一个节点指向反转后头节点
        tail  下一个节点是反转后尾节点链接

        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:  # 没有结束时候
            tail = pre  # 创造临时节点
            for i in range(k):
                tail = tail.next
                if not tail:  # 当不到k个时候，直接返回
                    return dummy.next
            nxt = tail.next  # 先把下一个节点找出
            head, tail = self.reverse(head, tail)
            pre.next = head  # 先链接头节点
            tail.next = nxt  # 尾节点和下一个节点链接
            pre = tail  # 移动pre节点
            head = nxt  # 移动head节点到新的待反转第一个位置
        return dummy.next

    def reverse(self, head, tail):  # 反转链表 返回头尾指针
        pre = tail.next  # 首先找到尾指针的下一个节点
        cur = head  # 临时节点充当头节点
        while pre != tail:  # 当反转节点没有到尾巴时候
            nxt = cur.next  # 指向当前节点下一节点
            cur.next = pre  # 反转指向
            pre = cur  # 反转指针移动
            cur = nxt  # 头指针移动
        return tail, head
