#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0] * len(nums)
        if len(nums) == 0:
            return
        self.sums[0] = nums[0]
        for i in range(1, len(nums)):
            self.sums[i] = nums[i] + self.sums[i - 1]

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            sub = 0
        else:
            sub = self.sums[i - 1]
        return self.sums[j] - sub


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

