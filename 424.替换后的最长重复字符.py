#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
from collections import Counter
# @lc code=start
class Solution:
    def check(self, s, k, char_max):
        ret = min(char_max + k, len(s))
        return ret
        
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 1
        max_ret = 0
        char_max = 0
        n = len(s)
        dic = {}
        while j <= n:
            dic.setdefault(s[j-1], 0)
            dic[s[j-1]] += 1
            char_max = max(char_max, dic[s[j-1]])
            ret = self.check(s[i:j], k, char_max)
            if ret > max_ret:
                max_ret = ret
                j += 1
            else:
                dic[s[i]] -= 1
                i += 1
                j += 1
        return max_ret

# @lc code=end

s = Solution()
s.characterReplacement("AABABBA", 1)