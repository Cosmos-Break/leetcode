#
# @lc app=leetcode.cn id=1175 lang=python3
#
# [1175] 质数排列
#

# @lc code=start
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        def factorial(x):
            if x <= 1:
                return x
            else:
                return x*factorial(x-1)
        A = [1]
        B = []
        for i in range(2, n+1):
            k = 0
            for j in range(2, i+1):
                if i % j == 0:
                    k += 1
            if k > 1:
                A.append(i)
            else:
                B.append(i)
        return (factorial(len(A)) * factorial(len(B))) % (10**9 + 7)

# @lc code=end

