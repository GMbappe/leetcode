# _*_coding:utf-8 _*_
# @Time    : 2022/7/17 11:18
# @Author  : Guo 
# @File    : 565. 数组嵌套.py
# @Desc    : https://leetcode.cn/problems/array-nesting/

"""
索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到最大的集合S并返回其大小，
其中 S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。
假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。

 
示例 1:
输入: A = [5,4,0,3,1,6,2]
输出: 4
解释:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
"""
class Solution:
    def arrayNesting(self, nums) -> int:
        """
        图循环，如果碰到已经访问过的则停止
        因为如果形成环 则环上任一点出发结果是相同的
        所以一次遍历即可
        """
        ans = 0
        n = len(nums)
        vis = [False] * n #标记已经访问过的数组
        for i in range(n):
            cur = 0 #当前位置开始遍历的长度
            while not vis[i]:
                vis[i] = True
                i = nums[i] #下一个位置
                cur += 1
            ans = max(ans, cur)
        return ans