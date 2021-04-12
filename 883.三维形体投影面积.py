#
# @lc app=leetcode.cn id=883 lang=python3
#
# [883] 三维形体投影面积
#

# @lc code=start
class Solution:
    def projectionArea(self, grid):
        N = len(grid)
        ans = 0

        for i in range(N):
            best_row = 0  # max of grid[i][j]
            best_col = 0  # max of grid[j][i]
            for j in range(N):
                if grid[i][j]: ans += 1  # top shadow
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])

            ans += best_row + best_col

        return ans

        """ Alternative solution:
        ans = sum(map(max, grid))
        ans += sum(map(max, zip(*grid)))
        ans += sum(v > 0 for row in grid for v in row)
        """
# @lc code=end

