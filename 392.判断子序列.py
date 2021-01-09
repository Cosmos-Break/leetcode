#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a_beg = -1
        a_end = len(t)
        fail = 0
        for a in s:
            a_beg = t.find(a, a_beg + 1, a_end)
            if a_beg == -1:
                return False
        return True
# @lc code=end
