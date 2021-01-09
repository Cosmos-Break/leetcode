#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
from typing import List
# @lc code=start

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         result = ''
#         i = 0
#         j = 0
#         try:
#             while True:
#                 while i < len(strs) - 1:
#                     if strs[i][j] != strs[i + 1][j]:
#                         return result
#                     i += 1
#                 result += strs[i][j]
#                 j += 1
#                 i = 0
#         except:
#             return result
#         finally:
#             return result

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''
        print(*strs)
        sz = zip(*strs)
        for s in sz:
            print(s)

        c = [(1, 2, 3), (4, 5, 6, 7)]
        
        print(*c)
        for a in zip(*c):
            print(a)

        # for a, *b in [(1, 2, 3), (4, 5, 6, 7)]:
        #     print(a)
        #     print(b)
        
# @lc code=end

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    s = Solution()
    result = s.longestCommonPrefix(strs)
    print(result)
