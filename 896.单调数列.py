#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

# @lc code=start
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def up(A):
            for i in range(1, len(A)):
                if A[i] < A[i - 1]:
                    return False
            return True
        def down(A):
            for i in range(1, len(A)):
                if A[i] > A[i - 1]:
                    return False
            return True
        return up(A) or down(A)
# @lc code=end

