#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        return int("0b"+("0"*32+bin(n)[2:])[-32:][::-1], base=2)
# @lc code=end

