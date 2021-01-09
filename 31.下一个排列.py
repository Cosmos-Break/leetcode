#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
from typing import List
# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return
        j = n - 2
        while nums[j] >= nums[j + 1] and j >= 0:
            j -= 1
        if j != -1:
            swap_index = j + 1
            i = n - 1
            while i >= 0:
                if nums[i] > nums[j]:
                    swap_index = i
                    break
                i -= 1
            nums[swap_index], nums[j] = nums[j], nums[swap_index]
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        reverse(nums, j + 1, n - 1)


# @lc code=end

s = Solution()
s.nextPermutation([2,3,1,3,3])