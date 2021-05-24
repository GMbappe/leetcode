# _*_coding:utf-8 _*_
# @Time    : 2021/5/24 22:47
# @Author  : Guo 
# @File    : 207. 课程表.py
# @Desc    : https://leetcode-cn.com/problems/course-schedule/
"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，
其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 
示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
"""
from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        使用优先队列  BFS
        1.创造邻接表表示每个节点的后继节点有哪些， 入度数组表示每个节点的入度数
        2. 将0 入度课程放入队列中
        3. 当队列不为空时，弹出队首元素，然后计数+1，然后这个元素的后继元素的入度都-1  如果某个点的入度为0则添加到队列中
        4. 最后判断 计数 == 课程数
        """
        if not numCourses:
            return True

        in_degree = [0 for _ in range(numCourses)]  # 入度数组
        adj = [set() for _ in range(numCourses)]  # 邻接表

        for i, j in prerequisites:  # j在i前面
            in_degree[i] += 1  # 入度+1
            adj[j].add(i)  # 添加后继节点

        queue = deque()
        for i in range(numCourses):  # 先将0入度的课程放入队列中
            if in_degree[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            cur = queue.popleft()  # 弹出队首元素
            count += 1
            for i in adj[cur]:  # 对于后继元素
                in_degree[i] -= 1  # 入度都要-1
                if in_degree[i] == 0:  # 如果入度为0 则入队列
                    queue.append(i)

        return count == numCourses