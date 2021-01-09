#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
        return max_sum

# @lc code=end
s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])


