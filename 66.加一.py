#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = ''
        for digit in digits:
            result += str(digit)
        result = str(int(result) + 1)
        result_list = []
        for digit in result:
            result_list.append(int(digit))
        return result_list
        
# @lc code=end

