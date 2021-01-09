#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start

class Solution:
    def lcp(self, str1, str2):
        min_len = min(len(str1), len(str2))
        ret_index = 0
        while ret_index < min_len and str1[ret_index] == str2[ret_index]:
            ret_index += 1
        return str1[:ret_index]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        start_s = strs[0]
        for s in strs[1:]:
            start_s = self.lcp(start_s, s)
            if start_s == "":
                return ""
        return start_s
        
# @lc code=end

strs = ["flower", "flow", "flight"]
s = Solution()
result = s.longestCommonPrefix(strs)
print(result)

# 求n个str的最长公共前缀 可以转化为两两求最长公共前缀
# 如果在求公共前缀的过程中产生了空字符串,则最后返回的一定是空字符串
