#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        l = len(haystack)
        for i in range(l - n + 1):
            if haystack[i:i + n] == needle:
                return i
        return -1

# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         n = len(needle)
#         l = len(haystack)
#         if n == 0:
#             return 0
#         for i in range(l - n + 1):
#             if haystack[i] == needle[0]:
#                 pl = i
#                 pn = 0
#                 while pn < n and haystack[pl] == needle[pn]:
#                     pn += 1
#                     pl += 1
#                 if pn == n:
#                     return pl - pn
#                 else:
#                     continue
#         return -1
# @lc code=end

# 子串逐一比较 - 线性时间复杂度
# 双指针 - 线性时间复杂度
s = Solution()
s.strStr("hello", "ll")