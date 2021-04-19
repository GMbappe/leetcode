# _*_coding:utf-8 _*_
# @Time    : 2020/12/25 0:06
# @Author  : Guo 
# @File    : 135. 分发糖果.py
# @Desc    : https://leetcode-cn.com/problems/candy/

"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
你需要按照以下要求，帮助老师给这些孩子分发糖果：
每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:
输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
"""


class Solution(object):
    def candy(self, ratings):
        """
        因为如果满足大于相邻，必须这个位置糖果数目更多
        1. 先从左遍历，遇到大于左边的，则该位置糖果应是左边糖果+1
        2. 从右遍历，遇到大于右边的 并且糖果小于等于右边，则该位置+1
        """
        n = len(ratings)
        left = [1] * n
        for i in range(n):
            if i > 0 and ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        print(left)
        right = ret = 0
        for i in range(n - 1, -1, -1):
            print(i)
            if i < n - 1 and ratings[i] > ratings[i + 1] and left[i] <= left[i+1]:
                left[i] = left[i+1] + 1

        print(left)

        return sum(left)


if __name__ == '__main__':
    ra = [1,3,4,5,2]
    s = Solution()
    s.candy(ra)