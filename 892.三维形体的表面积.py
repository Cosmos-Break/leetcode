# @before-stub-for-debug-begin
from python3problem892 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=892 lang=python3
#
# [892] 三维形体的表面积
#

# @lc code=start
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        ans = 0
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0
                        ans += max(grid[r][c] - nval, 0)
        return ans

# @lc code=end

