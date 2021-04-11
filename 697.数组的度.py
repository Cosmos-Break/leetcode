# @before-stub-for-debug-begin
from python3problem697 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=697 lang=python3
#
# [697] 数组的度
#

# @lc code=start
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_val = 0
        max_key = []
        for key, val in cnt.items():
            if val > max_val:
                max_val = val
                max_key = [key]
            elif val == max_val:
                max_key.append(key)
        return min(len(nums) - nums[::-1].index(key) - nums.index(key) for key in max_key)
# @lc code=end

