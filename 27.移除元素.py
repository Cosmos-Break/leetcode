#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(0, len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        nums = nums[:i]
        return len(nums)
# @lc code=end

# 双指针, 快慢指针, 注意 这个快指针j要从0开始 
# 因为0位置可能等于val
