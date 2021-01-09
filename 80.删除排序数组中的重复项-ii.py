#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        i = 2
        while i < len(nums):
            if nums[i] == nums[i - 1] == nums[i - 2]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
# @lc code=end
s = Solution()
s.removeDuplicates([1,1,1,2,2,3])
