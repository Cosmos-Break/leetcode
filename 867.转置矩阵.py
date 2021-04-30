#
# @lc app=leetcode.cn id=867 lang=python3
#
# [867] 转置矩阵
#

# @lc code=start
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        trans = [[0] * row for _ in range(col)]
        for j in range(col):
            for i in range(row):
                trans[j][i] = matrix[i][j]
        return trans
                

# @lc code=end

