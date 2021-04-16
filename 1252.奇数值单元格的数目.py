#
# @lc app=leetcode.cn id=1252 lang=python3
#
# [1252] 奇数值单元格的数目
#

# @lc code=start
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        matrix = [[0] * m for _ in range(n)]
        for x, y in indices:
            for i in range(n):
                matrix[i][y] += 1
            for j in range(m):
                matrix[x][j] += 1
        return sum(elem % 2 == 1 for line in matrix for elem in line)

# @lc code=end

