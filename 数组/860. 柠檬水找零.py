# _*_coding:utf-8 _*_
# @Time    : 2020/12/10 9:46
# @Author  : Guo 
# @File    : 860. 柠檬水找零.py
# @Desc    : https://leetcode-cn.com/problems/lemonade-change/
"""

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：
输入：[5,5,10]
输出：true

示例 3：
输入：[10,10]
输出：false

示例 4：
输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        因为支付的是5，10，20 所以20能用
        设置5，10元的数目，如果需要找零，优先减10元的
        """
        if not bills:
            return False

        five_cnt = 0
        ten_cnt = 0

        for bill in bills:
            if bill == 5:
                five_cnt += 1
            elif bill == 10:
                if five_cnt == 0:
                    return False
                five_cnt -= 1
                ten_cnt += 1
            else:
                if five_cnt > 0 and ten_cnt > 0:
                    five_cnt -= 1
                    ten_cnt -= 1
                elif five_cnt >= 3:
                    five_cnt -= 3
                else:
                    return False
        return True