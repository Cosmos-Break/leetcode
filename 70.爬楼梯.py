#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
# class Solution:
#     def __init__(self):
#         self.save_dict = {1:1, 2:2}
#     def climbStairs(self, n: int) -> int:
#         if n not in self.save_dict:
#             result = self.climbStairs(n - 1) + self.climbStairs(n - 2)
#             self.save_dict[n] = result
#             return result
#         else:
#             return self.save_dict[n]
class Solution:
    def climbStairs(self, n: int) -> int:
        i, j, k = 0, 0, 1
        for _ in range(n):
            i = j
            j = k
            k = i + j
        return k
# @lc code=end
# 动态规划 滚动数组思想
# 矩阵快速幂
# 通项公式
