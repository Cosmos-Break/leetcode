#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        m, n = 0, 1
        ret = [0] * len(nums)
        for num in nums:
            if num % 2 == 0:
                ret[m * 2] = num
                m += 1
            else:
                ret[n * 2 - 1] = num
                n += 1
        return ret
# @lc code=end

