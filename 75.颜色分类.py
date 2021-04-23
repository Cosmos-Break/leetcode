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
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[pointer_0] = nums[pointer_0], nums[i]
                pointer_0 += 1
        for i in range(n):
            if nums[i] == 1:
                nums[i], nums[pointer_0] = nums[pointer_0], nums[i]
                pointer_0 += 1
        
            
# @lc code=end
