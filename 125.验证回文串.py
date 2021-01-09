#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                result += char.lower()
        result_reverse = result[::-1]
        if result == result_reverse:
            return True
        else:
            return False
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.isPalindrome("A man, a plan, a canal: Panama")
