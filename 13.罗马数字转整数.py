#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'IV' : 4, 'IX' : 9,
            'XL' : 40, 'XC' : 90,
            'CD' : 400, 'CM' : 900,
            'I' : 1, 'V' : 5,
            'X' : 10, 'L' : 50,
            'C' : 100, 'D' : 500,
            'M' : 1000
        }
        result = 0
        i = 0
        while i < len(s) - 1:
            if (s[i] + s[i + 1]) in num_dict:
                result += num_dict[s[i] + s[i + 1]]
                i += 2
            else:
                result += num_dict[s[i]]
                i += 1
        if i == len(s) - 1:
            result += num_dict[s[i]]
        return result
# @lc code=end

