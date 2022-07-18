# _*_coding:utf-8 _*_
# @Time    : 2022/7/14 18:23
# @Author  : Guo 
# @File    : 208. 实现 Trie (前缀树).py
# @Desc    : https://leetcode.cn/problems/implement-trie-prefix-tree/
"""
Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。
请你实现 Trie 类：
Trie() 初始化前缀树对象。
void insert(String word) 向前缀树中插入字符串 word 。
boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。
 

示例：
输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True
"""


class TrieNode(object):
    def __init__(self):
        self._R = 26  # 因为是26个字母
        self.isEnd = False  # 表示是否结尾
        self.next = [None] * self._R # 表示节点的后续节点

    def containKeys(self, ch):
        return self.next[ord(ch) - ord('a')] is not None

    def put(self, ch, node):  #建立索引
        self.next[ord(ch) - ord('a')] = node

    def get(self, ch):
        return self.next[ord(ch) - ord('a')]


class Trie(object):
    def __init__(self):
        """
        初始化树结构
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        插入单词到树中
        :param word:
        :return:
        """
        node = self.root
        for w in word:
            if not node.containKeys(w):
                node.put(w, TrieNode())  # 不包含就建树
            node = node.get(w)
        node.isEnd = True  # 说明创建完成

    def searchPrefix(self, word):
        """
        搜索前缀是否在
        :param word:
        :return:
        """
        node = self.root
        for w in word:
            if node.containKeys(w):
                node = node.get(w)
            else:
                return None
        return node

    def search(self, word):
        #单词是否存在 必须结尾也是
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix):
        # 查看是否有单词是给定的索引
        node = self.searchPrefix(prefix)
        return node is not None