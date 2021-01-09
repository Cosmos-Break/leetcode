#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#
from typing import List
# @lc code=start
class Solution:
    # TLE
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     sum = nums[0] + nums[1] + nums[2]
    #     close_value = abs(sum - target)
    #     res = []
    #     for i in range(n):
    #         for j in range(i + 1, n):
    #             for k in range(j + 1, n):
    #                 temp = abs(nums[i] + nums[j] + nums[k] - target)
    #                 if close_value > temp:
    #                     close_value = temp
    #                     sum = nums[i] + nums[j] + nums[k]
    #     return sum
                    
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        sum_val = nums[0] + nums[1] + nums[2]
        close_value = abs(sum_val - target)
        for i in range(n):
            L = i + 1
            R = n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R] - target
                if temp == 0:
                    return target
                elif temp > 0:
                    if close_value > abs(temp):
                        sum_val = nums[i] + nums[L] + nums[R]
                        close_value = abs(temp)
                    R -= 1
                else:
                    if close_value > abs(temp):
                        sum_val = nums[i] + nums[L] + nums[R]
                        close_value = abs(temp)
                    L += 1
        return sum_val


# @lc code=end
s = Solution()
print(s.threeSumClosest([1,1,1,0], -100))
