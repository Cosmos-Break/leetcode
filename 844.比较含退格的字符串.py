#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def help(s):
            stack1 = []
            for char in s:
                if char == "#" and len(stack1) != 0:
                    stack1.pop()
                elif char != "#":
                    stack1.append(char)
            return stack1
        stack1 = help(s)
        stack2 = help(t)
        return stack1 == stack2
        
# @lc code=end

