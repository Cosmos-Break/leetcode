#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# from typing import List
# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pointer_0 = 0
        pointer_2 = n - 1
        i = 0
        while i <= pointer_2:
            if nums[i] == 2:
                nums[i], nums[pointer_2] = nums[pointer_2], nums[i]
                pointer_2 -= 1
            elif nums[i] == 0:
                nums[i], nums[pointer_0] = nums[pointer_0], nums[i]
                pointer_0 += 1
                i += 1
            else:
                i += 1
            
# @lc code=end
