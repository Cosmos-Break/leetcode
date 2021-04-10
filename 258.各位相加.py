#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        def pending_num(num):
            sum = 0
            while num:
                sum += num % 10
                num //= 10
            return sum
        while num >= 10:
            num = pending_num(num)
        return num
# @lc code=end

