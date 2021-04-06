#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        ret = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                ret.append(i)
        return ret
# @lc code=end

