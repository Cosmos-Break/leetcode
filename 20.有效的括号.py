#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {
            ')':'(', '}':'{', ']':'['
        }
        for char in s:
            if char not in dic:
                stack.append(char)
            elif stack:
                char_pop = stack.pop()
                if char_pop != dic[char]:
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.isValid("()")

