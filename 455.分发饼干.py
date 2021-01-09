#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        i, j = 0, 0
        ret = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                ret += 1
                i += 1
            j += 1
            
        return ret

# @lc code=end
