#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        dp = [[False] * n for _ in range(n)]
        for l in range(1, n + 1):
            for i in range(n):
                j = i + l - 1
                if j >= n:
                    break
                if l == 1:
                    dp[i][j] = True
                elif l == 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                if l > len(ans) and dp[i][j]:
                    ans = s[i:j+1]
        return ans


# @lc code=end
# DP, 如果只有一个字符, 为回文
# 如果有两个字符, 判断两个字符是否相同, 相同则为回文
# 大于两个字符, 比较首尾是否相同 和 去掉首尾之后是否是回文.
# 终止条件 结尾>=len(s)
