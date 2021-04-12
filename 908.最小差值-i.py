#
# @lc app=leetcode.cn id=908 lang=python3
#
# [908] 最小差值 I
#

# @lc code=start
class Solution(object):
    def smallestRangeI(self, A, K):
        return max(0, max(A) - min(A) - 2*K)

# @lc code=end

