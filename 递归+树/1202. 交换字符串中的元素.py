# _*_coding:utf-8 _*_
# @Time    : 2021/1/11 21:58
# @Author  : Guo 
# @File    : 1202. 交换字符串中的元素.py
# @Desc    : https://leetcode-cn.com/problems/smallest-string-with-swaps/
"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。
 
示例 1:
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
"""


class Solution(object):
    """
    构建连通图，如果配对出现，说明两个点是有边的
    找到哪些点是连通的，可以使用bfs进行寻找
    然后再一个集合的点位进行排序，再放到原来的位置中即可
    """
    def smallestStringWithSwaps(self, s, pairs):
        # 构建图
        graph = [[] for _ in range(len(s))]
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        res = list(s)
        visited = [0] * len(s)
        for i in range(len(s)):
            if not visited[i]: # 如果没有被访问过 
                # 获取当前节点联通点
                connect_node = []
                self.dfs(connect_node, graph, visited, i)
                # 重新赋值
                index = sorted(connect_node)  # 对分组的索引进行排序
                st = sorted(res[j] for j in index)  # 对分组的字母进行排序
                for p, q in zip(index, st):
                    res[p] = q
        return "".join(res)

    def dfs(self, res, graph, visited, i):
        for j in graph[i]:
            if not visited[j]:
                visited[j] = 1
                res.append(j)
                self.dfs(res, graph, visited, j)