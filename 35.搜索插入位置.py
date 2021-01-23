#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
from typing import List
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            # mid = left + (right - left) // 2
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
# @lc code=end

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         left, right = 0, len(nums)
#         while left < right:
#             mid = left + (right - left) // 2
#             if nums[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid
#         return left

# 二分查找模板
# mid = (left + right) // 2 也可
s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))


