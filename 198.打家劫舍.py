#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # i = 0
        # result_0 = 0
        # result_1 = 0
        # while i < len(nums):
        #     if i % 2 == 0:
        #         result_0 += nums[i]
        #     else:
        #         result_1 += nums[i]
        #     i += 1
        # return max(result_0, result_1)
        max_3_house_before, max_2_house_before, adjacent = 0, 0, 0
        for cur in nums:
            max_3_house_before, max_2_house_before, adjacent = \
            max_2_house_before, adjacent, max(max_3_house_before+cur, max_2_house_before+cur)
        return max(max_2_house_before, adjacent)
# @lc code=end

