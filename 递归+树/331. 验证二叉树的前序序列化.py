# _*_coding:utf-8 _*_
# @Time    : 2021/3/13 0:04
# @Author  : Guo 
# @File    : 331. 验证二叉树的前序序列化.py
# @Desc    : https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 #。

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
例如，上面的二叉树可以被序列化为字符串 "9,3,4,#,#,1,#,#,2,#,6,#,#"，其中 # 代表一个空节点。
给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。
每个以逗号分隔的字符或为一个整数或为一个表示 null 指针的 '#' 。
你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 "1,,3" 。

示例 1:
输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
"""


class Solution:
    def isValidSerialization(self, preorder) -> bool:
        """
        辅助栈，
        顺序遍历，如果出现 数字 # # 的时候，说明这个是有效叶节点，可以直接合并 当作# 放入栈中
        遍历接收后，查看栈中是否只剩一个#
        """
        stack = []
        pre = preorder.split(',')
        for i in pre:
            stack.append(i)
            if stack:
                while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                    stack.pop(), stack.pop(), stack.pop()
                    stack.append('#')

        return len(stack) == 1 and stack[-1] == '#'