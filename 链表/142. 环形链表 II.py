# _*_coding:utf-8 _*_
# @Time    : 2021/5/16 18:20
# @Author  : Guo 
# @File    : 142. 环形链表 II.py
# @Desc    : https://leetcode-cn.com/problems/linked-list-cycle-ii/
"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
进阶：
你是否可以使用 O(1) 空间解决此题？
 
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        """
        方法一：利用hashset，如果节点没有存在在hashset中，则添加
        当第一次出现重复时，就为入口

        方法二：快慢指针
        在第一次相遇时候， 假设 a 为环之前的距离，b为环的长度 a+b为整个长度
        f = 2s （快指针每次走两倍于慢指针）
        f = s + nb (第一次相遇时，快指针和慢指针在圈内循环n倍)
         ==》s = nb 下来只让慢指针走a 步即可，再在头节点一直指针，和慢指针同时走，相遇时，即在入口处
        """

        fast = head
        slow = head
        while True:
            if not (fast and fast.next): return  # 不存在环
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        pre = head
        while pre != slow:
            pre = pre.next
            slow = slow.next
        return pre