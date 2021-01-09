#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于K的子数组
#
from typing import List
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # TLE
        # i = 0
        # j = 0
        # product = 1
        # n = len(nums)
        # ret = 0
        # while i < n:
        #     product *= nums[j]
        #     if product < k:
        #         # print(nums[i:j+1])
        #         ret += 1
        #         j += 1
        #         if j == n and i < n:
        #             product = 1
        #             i += 1
        #             j = i
        #     else:
        #         product = 1
        #         i += 1
        #         j = i
        # return ret
        
        # if k <= 1:
        #     return 0
        # left = 0
        # n = len(nums)
        # product = 1
        # ret = 0
        # for right, val in enumerate(nums):
        #     product *= val
        #     while product >= k:
        #         product /= nums[left]
        #         left += 1
        #     ret += right - left + 1
        # return ret

    

        
                

# @lc code=end
s = Solution()
s.numSubarrayProductLessThanK([10,5,2,6],100)
