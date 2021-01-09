#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(1, rowIndex+1):
            for j in range(1, i):
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
        return result[rowIndex]
# @lc code=end

