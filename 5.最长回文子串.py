#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start



class Solution:
    # def isPalindrome(self, s):
    #     if s == s[::-1]:
    #         return True
    #     else:
    #         return False

    # def longestPalindrome(self, s: str) -> str:
    #     if s == "":
    #         return ""
    #     max_len = 1
    #     max_len_string = s[0]
    #     for i in range(len(s)):
    #         for j in range(i + 1, len(s) + 1):
    #             string = s[i:j]
    #             if self.isPalindrome(string):
    #                 if max_len < len(string):
    #                     max_len = len(string)
    #                     max_len_string = string
    #     return max_len_string 
    def longestPalindrome(self, s: str) -> str:
        max_len_substring = ""
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for l in range(n): # 枚举子串长度, l = 0 表示子串长度为 1
            for i in range(n):  # 枚举子串的起始位置
                j = l + i
                if j >= n:
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i+1][j-1] is True and s[i] == s[j])
                if dp[i][j] is True and l + 1 > len(max_len_substring):
                    max_len_substring = s[i:j + 1]
        return max_len_substring
                

    
# @lc code=end
# if __name__ == "__main__":
#     s = Solution()
#     s.longestPalindrome("bb")

