# @before-stub-for-debug-begin
from python3problem34 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ret_l, ret_r = -1, -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ret_l = mid
                ret_r = mid
                while ret_l - 1 >= 0 and nums[ret_l - 1] == target:
                    ret_l -= 1
                while ret_r + 1 < len(nums) and nums[ret_r + 1] == target:
                    ret_r += 1
                return [ret_l, ret_r]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [ret_l, ret_r]
# @lc code=end

