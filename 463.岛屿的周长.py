# @before-stub-for-debug-begin
from python3problem463 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#

# @lc code=start
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        diff = [[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt = 0
                    for k in range(4):
                        dx = i + diff[k][0]
                        dy = j + diff[k][1]
                        if dx < 0 or dy < 0 or dx >= n or dy >= m or grid[dx][dy] == 0:
                            cnt += 1
                    ans += cnt
        return ans
# @lc code=end

