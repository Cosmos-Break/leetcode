#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = nums[0]
        for num in nums[1:]:
            result = result ^ num
        return result
        
# @lc code=end

