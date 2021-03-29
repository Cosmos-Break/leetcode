# @before-stub-for-debug-begin
from python3problem509 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        i = 0
        j = 1
        k = 1
        for m in range(n - 1):
            k = i + j
            i = j
            j = k
        return k

# @lc code=end

