#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List
from itertools import permutations

# @lc code=start
class Solution:
    # TLE
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     def in_list(i, j, k, res):
    #         for item in permutations([i, j, k], 3):
    #             if list(item) in res:
    #                 return True
    #         return False
            
    #     n = len(nums)
    #     res = []
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             for k in range(j + 1, n):
    #                 if nums[i] + nums[j] + nums[k] == 0:
    #                     if not in_list(nums[i], nums[j], nums[k],res):
    #                         res.append([nums[i], nums[j], nums[k]])  
    #     return res
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            L = i + 1
            R = n - 1
            while L < R:
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1
                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1
                    L += 1
                    R -= 1
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                else:
                    L += 1
        return res
# @lc code=end
# s = Solution()
# nums = [-1,0,1,2,-1,-4]
# print(s.threeSum(nums))
