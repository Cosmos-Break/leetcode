#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, num in enumerate(nums):
            if num < target:
                continue
            else:
                return index
        return len(nums)
# @lc code=end

