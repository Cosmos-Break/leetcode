#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        x_list_reverse = reversed(x_list)
        for i, j in zip(x_list, x_list_reverse):
            if i != j:
                return False
        
        return True
# @lc code=end

