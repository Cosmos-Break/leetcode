#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        N = bin(N)[2:]
        N = N.replace("0","2")
        N = N.replace("1","0")
        N = N.replace('2','1')
        return int(N,2)

# @lc code=end

