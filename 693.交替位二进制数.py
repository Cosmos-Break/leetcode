#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_str = bin(n)[2:]
        return all(bin_str[i-1]!= bin_str[i] for i in range(1,len(bin_str)))

# @lc code=end

