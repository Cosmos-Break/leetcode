#
# @lc app=leetcode.cn id=796 lang=python3
#
# [796] 旋转字符串
#

# @lc code=start
class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A

# @lc code=end

