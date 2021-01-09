#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#
from typing import List
import bisect
# @lc code=start
class Solution:
    # def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    #     i, j = 0, 0
    #     n = len(nums)
    #     min_len = n
        
    #     if sum(nums) < s:
    #         return 0
        
    #     current_num = nums[0]
    #     while j < n:
    #         if current_num < s:
    #             j += 1
    #             if j < n:
    #                 current_num += nums[j]
    #         else:
    #             min_len = min(min_len, j - i + 1)
    #             current_num -= nums[i]
    #             i += 1
    #     return min_len

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        # 求前缀和
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        #print(nums)
        # 总和都小于 s 时候
        if nums[-1] < s: return 0
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                # 二分查找
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res 

# @lc code=end
s = Solution()
s.minSubArrayLen(7, [2,3,1,2,4,3])

