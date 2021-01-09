#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        change_num_dict = {
            'IV' : "IIII", 'IX' : "IIIIIIIII",
            'XL' : "XXXX", 'XC' : "XXXXXXXXX",
            'CD' : "CCCC", 'CM' : "CCCCCCCCC",
        }
        num_dict = {
            'I' : 1, 'V' : 5,
            'X' : 10, 'L' : 50,
            'C' : 100, 'D' : 500,
            'M' : 1000
        }
        for key, val in change_num_dict.items():
            if key in s:
                s = s.replace(key, val)
        
        sum = 0
        for char in s:
            sum += num_dict[char]
        return sum
        
# @lc code=end
# 先把特殊数字转化为一般数字, 之后统一处理