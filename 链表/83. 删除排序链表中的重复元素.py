# _*_coding:utf-8 _*_
# @Time    : 2021/3/25 23:13
# @Author  : Guo 
# @File    : 83. 删除排序链表中的重复元素.py
# @Desc    : https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

"""
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。
返回同样按升序排列的结果链表。

示例 1：
输入：head = [1,1,2]
输出：[1,2]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        用cur 指向head 对 cur进行操作
        如果当前节点值== 下一个节点值，则当前节点下一个节点指向下下个节点
        否则当前节点指向 下一个节点 移动
        :param head:
        :return:
        """
        if not head:
            return head

        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head