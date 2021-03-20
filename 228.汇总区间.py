# @before-stub-for-debug-begin
from python3problem228 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        ret = []
        while i < len(nums):
            low = i
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]+1:
                i += 1
            high = i - 1
            if low < high:
                ret.append(str(nums[low])+'->'+str(nums[high]))
            else:
                ret.append(str(nums[low]))
        return ret
        

# @lc code=end

