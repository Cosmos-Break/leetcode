#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#
from typing import List
# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right = n, n
        result_list = []
        result = ''
        def generate(left, right, result, result_list):
            if len(result) == 2 * n:
                result_list.append(result)
                return
            if left > 0:
                generate(left - 1, right, result + '(', result_list)
            if right > left:
                generate(left, right - 1, result + ')', result_list)
        generate(n, n, result, result_list)
        return result_list
                
# @lc code=end
s = Solution()
s.generateParenthesis(3)
