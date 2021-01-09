#
# @lc app=leetcode.cn id=532 lang=python3
#
# [532] 数组中的K-diff数对
#

# @lc code=start
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        ret = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + k in nums[i+1:]:
                ret += 1
        return ret
            
# @lc code=end

