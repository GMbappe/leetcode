# _*_coding:utf-8 _*_
# @Time    : 2021/1/13 22:10
# @Author  : Guo 
# @File    : 684. 冗余连接.py
# @Desc    : https://leetcode-cn.com/problems/redundant-connection/
"""
在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

示例 1：

输入: [[1,2], [1,3], [2,3]]
输出: [2,3]
解释: 给定的无向图为:
  1
 / \
2 - 3
"""

"""
在一棵树中，边的数量比节点的数量少 11。如果一棵树有 NN 个节点，则这棵树有 N-1N−1 条边。这道题中的图在树的基础上多了一条附加的边，因此边的数量也是 NN。
树是一个连通且无环的无向图，在树中多了一条附加的边之后就会出现环，因此附加的边即为导致环出现的边。
可以通过并查集寻找附加的边。初始时，每个节点都属于不同的连通分量。遍历每一条边，判断这条边连接的两个顶点是否属于相同的连通分量。

如果两个顶点属于不同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间不连通，因此当前的边不会导致环出现，合并这两个顶点的连通分量。
如果两个顶点属于相同的连通分量，则说明在遍历到当前的边之前，这两个顶点之间已经连通，因此当前的边导致环出现，为附加的边，将当前的边作为答案返回
"""


class Solution:
    def findRedundantConnection(self, edges):
        nodesCount = len(edges)
        parent = list(range(nodesCount + 1))

        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        for node1, node2 in edges:
            if find(node1) != find(node2):
                union(node1, node2)
            else:
                return [node1, node2]
        return []


if __name__ == '__main__':
    a = [[1,2], [1,3], [2,3]]
    s = Solution()
    print(s.findRedundantConnection())
