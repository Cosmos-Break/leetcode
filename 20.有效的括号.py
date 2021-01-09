#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack or stack[-1] != pairs[char]:
                    return False
                else:
                    stack.pop(-1)
        return not stack
# @lc code=end
if __name__ == "__main__":
    s = Solution()
    s.isValid("()")

# 使用栈. 为了快速地配对括号, 使用了哈希表(字典)
# 如果是左括号 则不管啥就入栈, 如果是右括号, 判断一下栈里是否还有元素 栈顶元素是否为对应括号,
# 如果是,则出栈这个左括号, 如果不是则返回False
# 最后判断一下栈是否为空, 如果空 则返回True