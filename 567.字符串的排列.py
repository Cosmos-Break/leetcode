#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#
from itertools import permutations
# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TLE
        # for s in permutations(list(s1)):
        #     s = ''.join(s)
        #     if s in s2:
        #         return True
        # return False
        s1 = sorted(s1)
        s1_len = len(s1)
        s2_len = len(s2)
        for i in range(s1_len, s2_len + 1):
            tmp = sorted(s2[i - s1_len:i])
            if s1 == tmp:
                return True
        return False
# @lc code=end
