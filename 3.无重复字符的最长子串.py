#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if s == "":
    #         return 0
    #     max_len = 1
    #     for i in range(len(s)):
    #         result = ""
    #         for j in range(i, len(s)):
    #             if s[j] not in result:
    #                 result += s[j]
    #             else:
    #                 break
    #         max_len = max(len(result), max_len)
    #     return max_len
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        n = len(s)
        rk = -1
        ans = 0
        for i in range(n):
            if i != 0:
                chars.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in chars:
                chars.add(s[rk + 1])
                rk += 1
            ans = max(ans, len(chars))
        return ans

# @lc code=end
# s = Solution()
# print(s.lengthOfLongestSubstring("au"))
