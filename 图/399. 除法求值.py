# _*_coding:utf-8 _*_
# @Time    : 2021/1/6 22:11
# @Author  : Guo 
# @File    : 399. 除法求值.py
# @Desc    : https://leetcode-cn.com/problems/evaluate-division/
"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，其中 equations[i] = [Ai, Bi] 和 values[i]
共同表示等式 Ai / Bi = values[i] 。每个 Ai 或 Bi 是一个表示单个变量的字符串。
另有一些以数组 queries 表示的问题，其中 queries[j] = [Cj, Dj] 表示第 j 个问题，请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。
返回 所有问题的答案 。如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。


示例 1：
输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]
"""


class Solution:
    def calcEquation(self, equations, values, queries):
        """
        1. 用hashmap存储地图 graph[i][j] 表示 i/j 的值  就是i 到 j的边权重   等于中间点  graph[i][k] * graph[k][j]
        2. 用floyd算法计算 每个点到另一个点的最短距离
        """
        if not queries:
            return []

        from collections import defaultdict
        graph = defaultdict(int)
        node = set()
        n = len(equations)
        for i in range(n):  # 构造图
            x, y = equations[i]
            graph[(x, y)] = values[i]
            graph[(y, x)] = 1 / values[i]
            node.add(x)
            node.add(y)

        arr = list(node)
        for k in arr:  # floyd算法
            for i in arr:
                for j in arr:
                    if graph[(i, k)] and graph[(k, j)]:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]

        res = []
        for x, y in queries:
            if graph[(x, y)]:
                res.append(graph[(x, y)])
            else:
                res.append(-1)

        return res