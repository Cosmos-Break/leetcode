# @before-stub-for-debug-begin
from python3problem392 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 , p2 = 0, 0
        while p1 < len(s) and p2 < len(t):
            if s[p1] != t[p2]:
                p2 += 1
            else:
                p1 += 1
                p2 += 1
        return p1 == len(s)
# @lc code=end
