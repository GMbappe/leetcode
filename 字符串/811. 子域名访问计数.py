# _*_coding:utf-8 _*_
# @Time    : 2022/10/6 22:39
# @Author  : Guo 
# @File    : 811. 子域名访问计数.py
# @Desc    : https://leetcode.cn/problems/subdomain-visit-count/
"""
网站域名 "discuss.leetcode.com" 由多个子域名组成。顶级域名为 "com" ，二级域名为 "leetcode.com" ，最低一级为 "discuss.leetcode.com" 。
当访问域名 "discuss.leetcode.com" 时，同时也会隐式访问其父域名 "leetcode.com" 以及 "com" 。
计数配对域名 是遵循 "rep d1.d2.d3" 或 "rep d1.d2" 格式的一个域名表示，其中 rep 表示访问域名的次数，d1.d2.d3 为域名本身。
例如，"9001 discuss.leetcode.com" 就是一个 计数配对域名 ，表示 discuss.leetcode.com 被访问了 9001 次。
给你一个 计数配对域名 组成的数组 cpdomains ，解析得到输入中每个子域名对应的 计数配对域名 ，并以数组形式返回。可以按 任意顺序 返回答案。


示例 1：
输入：cpdomains = ["9001 discuss.leetcode.com"]
输出：["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
解释：例子中仅包含一个网站域名："discuss.leetcode.com"。
按照前文描述，子域名 "leetcode.com" 和 "com" 都会被访问，所以它们都被访问了 9001 次。
"""

from collections import defaultdict


class Solution:
    def subdomainVisits(self, cpdomains):
        "模拟，正常遍历"
        domain_dict = defaultdict(int)
        for i in cpdomains:
            num = i.split(" ")[0]
            domain_list = i.split(" ")[1].split(".")
            n = len(domain_list)
            for j in range(n):
                key = '.'.join(domain_list[j:])
                domain_dict[key] += int(num)
        ans = []
        for k, v in domain_dict.items():
            res = str(v) + " " + str(k)
            ans.append(res)

        return ans