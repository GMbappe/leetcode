# _*_coding:utf-8 _*_
# @Time    : 2022/10/2 10:04
# @Author  : Guo 
# @File    : 777. 在LR字符串中交换相邻字符.py
# @Desc    : https://leetcode.cn/problems/swap-adjacent-in-lr-string/
"""
在一个由 'L' , 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。
一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，
请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。

示例 :
输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
"""


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        使用双指针，查看start 和 end 中字符的相对顺序是否符合规则
        因为XL替换为LX  XR替换为RX
        所以 end中 L的下标必须小于等于start中的
                   R的下标必须大于等于start中的
        """
        i = 0
        j = 0
        n = len(start)
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == "X":
                j += 1

            if i < n and j < n:
                if start[i] != end[j]:
                    return False
                if (start[i] == "L" and i < j) or (start[i] == 'R' and i > j):
                    return False
                i += 1
                j += 1
        # 此时有一个下标遍历到结尾，则看另一个，如果其剩余的下标字符不为X 则返回False
        while i < n:
            if start[i] != "X":
                return False
            i += 1

        while j < n:
            if end[j] != "X":
                return False
            j += 1

        return True

