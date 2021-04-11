#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        counts = []
        i = 0
        while i < len(s):
            cnt = 0
            char = s[i]
            while i < len(s) and s[i] == char:
                cnt += 1
                i += 1
            counts.append(cnt)
        
        ret = 0
        for i in range(1, len(counts)):
            ret += min(counts[i-1], counts[i])
        return ret
# @lc code=end

