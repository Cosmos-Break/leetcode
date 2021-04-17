#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心下标
#

# @lc code=start
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        _sum = 0
        for i in range(len(nums)):
            if _sum * 2 + nums[i] == total:
                return i
            _sum += nums[i]
        return -1
# @lc code=end

