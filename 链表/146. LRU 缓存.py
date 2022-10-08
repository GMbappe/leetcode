# _*_coding:utf-8 _*_
# @Time    : 2022/8/16 20:47
# @Author  : Guo 
# @File    : 146. LRU 缓存.py
# @Desc    : https://leetcode.cn/problems/lru-cache/
"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；
如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 
示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
"""


class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        self.cache = dict()  # 用哈希表
        # 使用伪头部和伪尾部节点 双向链表
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.next = self.head
        self.capacity = capacity
        self.size = 0  # 长度需要和capacity进行对比

    def get(self, key):
        if key not in self.cache:
            return -1
            # 如果存在，先通过哈希表返回，然后再调整位置，到头节点
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value) -> None:
        if key not in self.cache:
            # 如果key不在，则创建一个新节点
            node = DLinkedNode(key, value)
            # 添加进hash表
            self.cache[key] = node
            # 添加至双链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 超出容量，删除尾节点
                removed = self.removeTail()
                self.cache.remove(removed.key())  # 删除hash表该key
                self.size -= 1
        else:
            # 如果在，则进行更新，并移动到头节点
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node):
        self.removeNode(node)  # 先移除
        self.addToHead(node)  # 再添加

    def removeNode(self, node):  # 移除该节点
        node.prev.next = node.next  # node节点前节点指向node后
        node.next.pre = node.prev  # node后节点的前节点指向node的前节点

    def addToHead(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node  # 移动node的头节点到后面
        self.head.next = node

    def removeTail(self):
        node = self.tail.prev  # 先找到尾部的前节点
        self.removeNode(node)
        return node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)