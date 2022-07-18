# _*_coding:utf-8 _*_
# @Time    : 2022/7/18 11:58
# @Author  : Guo 
# @File    : 749. 隔离病毒.py
# @Desc    : https://leetcode.cn/problems/contain-virus/

"""
病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。
假设世界由 m x n 的二维矩阵 isInfected 组成， isInfected[i][j] == 0 表示该区域未感染病毒，
而  isInfected[i][j] == 1 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。
每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，
每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 保证唯一 。
你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数;
如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。

"""


class Solution:
    def containVirus(self, isInfected) -> int:
        """
        bfs
        """
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 搜索的四个方向
        m = len(isInfected)
        n = len(isInfected[0])
        ans = 0

        while True:
            neighbors = list()  # 表示病毒的邻居
            firefalls = list()  # 表示病毒需要防火墙的数目   都是列表 表示每一块区域的病毒
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1:
                        q = deque([(i, j)])
                        neighbor = set()  # 这个区域病毒的邻居
                        firefall = 0  # 这个区域病毒防火墙数目
                        idx = len(neighbors) + 1  # 表示第几块区域
                        isInfected[i][j] = -idx  # 表示搜索过

                        while q:
                            x, y = q.popleft()
                            for p in range(4):
                                x_, y_ = x + dirs[p][0], y + dirs[p][1]  # 搜索的四个方向
                                if 0 <= x_ < m and 0 <= y_ < n:
                                    if isInfected[x_][y_] == 1:  # 如果是病毒则添加队列
                                        q.append((x_, y_))
                                        isInfected[x_][y_] = -idx
                                    elif isInfected[x_][y_] == 0:
                                        firefall += 1
                                        neighbor.add((x_, y_))
                        neighbors.append(neighbor)
                        firefalls.append(firefall)

            if not neighbors:  # 如果没有病毒区域 直接返回答案
                break

                # 找寻影响区域最大的病毒
            idx = 0
            for i in range(1, len(neighbors)):
                if len(neighbors[i]) > len(neighbors[idx]):
                    idx = i

            ans += firefalls[idx]  # 封锁这个病毒需要的防火墙数目

            # 将之前的标记复原
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] < 0:
                        if isInfected[i][j] != -idx - 1:  # 说明此区域病毒不是最大的
                            isInfected[i][j] = 1
                        else:
                            isInfected[i][j] = 2  # 最大区域病毒改变标记，不影响下次循环
            # 复原病毒周边邻居
            for i, neighbor in enumerate(neighbors):
                if i != idx:  # 说明不是最大病毒的周边，则被感染
                    for x, y in neighbor:
                        isInfected[x][y] = 1

            if len(neighbors) == 1:
                break

        return ans





