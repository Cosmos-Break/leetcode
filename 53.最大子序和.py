#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        premax = nums[0]
        truemax = nums[0]
        for num in nums[1:]:
            premax = max(premax + num, num)
            truemax = max(premax, truemax)
        return truemax
# @lc code=end
s = Solution()
s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
# 动态规划 先判断 只去当前值,还是取当前值+之前的值
# 然后取一个真正的更大值

