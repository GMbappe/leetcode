# _*_coding:utf-8 _*_
# @Time    : 2022/8/4 21:51
# @Author  : Guo 
# @File    : 剑指 Offer 35. 复杂链表的复制.py
# @Desc    : https://leetcode.cn/problems/fu-za-lian-biao-de-fu-zhi-lcof/

"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，
每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。


示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head):
        """
        1.创建 hashmap 存储映射关系
        2.复制 节点值
        3.复制 指向(next,random)
        """
        if not head:
            return None

        h = dict()
        pre = head
        while pre:
            h[pre] = Node(pre.val)
            pre = pre.next
        # 复制指向
        cur = head
        while cur:
            if cur.next:
                h[cur].next = h[cur.next] #新结点next指向同旧结点的next指向
            if cur.random:
                h[cur].random = h[cur.random] #新结点random指向同旧结点的random指向
            cur = cur.next

        return h[head]