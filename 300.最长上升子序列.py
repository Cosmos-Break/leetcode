#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# from typing import List
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # dp[i]的值代表以nums[i]结尾的最长子序列长度
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1) 
        return max(dp)

# @lc code=end
# if __name__ == "__main__":
#     s = Solution()
#     s.lengthOfLIS([10,9,2,5,3,4])