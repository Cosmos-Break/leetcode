#
# @lc app=leetcode.cn id=1030 lang=python3
#
# [1030] 距离顺序排列矩阵单元格
#

# @lc code=start
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = []
        for i in range(R):
            for j in range(C):
                matrix.append([i,j])
        return sorted(matrix, key=lambda x:abs(x[0]-r0) + abs(x[1]-c0))
# @lc code=end

