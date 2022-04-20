# _*_coding:utf-8 _*_
# @Time    : 2022/4/20 21:24
# @Author  : Guo 
# @File    : 388. 文件的最长绝对路径.py
# @Desc    :
"""
输入：input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
输出：20
解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20

"""


class Solution:
    def lengthLongestPath(self, input) -> int:
        """
        用 depth_length_map 保留每层路径的长度， input.split('\n') 切分为每行  分析每行长度与文件
        line.count('\t') 的个数来判断是第几层
        line.count('.') 的个数判断是否有文件，有文件获取当前最长路径值
        每层都要添加depth个 / ， 长度需要修改
        """
        res = 0
        depth_length_map = {-1: 0}
        for line in input.split('\n'):
            depth = line.count('\t')
            # 每行空格最后要被去掉
            depth_length_map[depth] = depth_length_map[depth - 1] + len(line) - depth
            if line.count('.'):
                # 每层都要添加depth个 /
                res = max(res, depth_length_map[depth] + depth)
        return res