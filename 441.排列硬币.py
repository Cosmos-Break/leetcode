#
# @lc app=leetcode.cn id=441 lang=python3
#
# [441] 排列硬币
#

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            guess = (1+mid) * mid // 2
            if guess == n:
                return mid
            elif guess < n:
                left = mid + 1
            else: right = mid -1
        return left - 1
# @lc code=end

