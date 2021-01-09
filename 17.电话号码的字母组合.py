#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#
# from typing import List
# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_dict = {
            2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl',
            6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'
        }
        if digits == "":
            return []
        result_list = []
        result = ""
        n = len(digits)
        def generate(digits, result):
            if len(result) == n:
                result_list.append(result)
                return
            digit = int(digits[0])
            for letter in num_dict[digit]:
                generate(digits[1:], result + letter)
        generate(digits, result)
        return result_list
# @lc code=end
# s = Solution()
# s.letterCombinations("23")
