#
# @lc app=leetcode.cn id=674 lang=python3
#
# [674] 最长连续递增序列
#

# @lc code=start
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cnt = 1
        max_cnt = 1
        for i in range(0, len(nums) - 1):
            if nums[i] < nums[i + 1]:
                cnt += 1
                max_cnt = max(max_cnt, cnt)
            else:
                cnt = 1
        return max_cnt
# @lc code=end

