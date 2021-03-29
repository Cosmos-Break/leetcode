#
# @lc app=leetcode.cn id=592 lang=python3
#
# [592] 分数加减运算
#

# @lc code=start
class Solution:
    def fractionAddition(self, expression: str) -> str:
        from re import findall
        from functools import reduce
        from math import gcd

        def calculate(m, n):
            divide1, divisor1 = map(int, m.split('/'))
            divide2, divisor2 = map(int, n.split('/'))
            lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)  # 最小公倍数
            divide = divide1 * (lcm // divisor1) + divide2 * (lcm // divisor2)
            _gcd = gcd(divide, lcm)  # 用于约分的最大公因数
            return f'{divide //_gcd}/{lcm // _gcd}'

        return reduce(calculate, findall('[+-]?\d+/\d+', expression))
# @lc code=end

