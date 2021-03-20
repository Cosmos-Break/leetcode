#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

# @lc code=end

