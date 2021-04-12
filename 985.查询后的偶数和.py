#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 查询后的偶数和
#

# @lc code=start
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        S = sum(x for x in A if x % 2 == 0)
        ans = []

        for x, k in queries:
            if A[k] % 2 == 0: S -= A[k]
            A[k] += x
            if A[k] % 2 == 0: S += A[k]
            ans.append(S)

        return ans

# @lc code=end

