#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                L = j + 1
                R = n - 1
                while L < R:
                    temp = nums[i] + nums[j] + nums[L] + nums[R]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        while L < R and nums[L] == nums[L + 1]:
                            L = L + 1
                        while L < R and nums[R] == nums[R - 1]:
                            R = R - 1
                        L += 1
                        R -= 1
                    elif temp < target:
                        L += 1
                    else:
                        R -= 1
        return res
                
# @lc code=end
s = Solution()
s.fourSum([0,0,0,0], 0)
