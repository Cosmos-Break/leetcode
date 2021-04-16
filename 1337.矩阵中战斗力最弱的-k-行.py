#
# @lc app=leetcode.cn id=1337 lang=python3
#
# [1337] 矩阵中战斗力最弱的 K 行
#

# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        n = len(mat)
        power = [sum(line) for line in mat]
        ans = list(range(n))
        ans.sort(key=lambda i: (power[i], i))
        return ans[:k]

# @lc code=end

