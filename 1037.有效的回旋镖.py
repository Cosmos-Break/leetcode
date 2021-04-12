#
# @lc app=leetcode.cn id=1037 lang=python3
#
# [1037] 有效的回旋镖
#

# @lc code=start
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False
        a = [points[1][0] - points[0][0], points[1][1] - points[0][1]]
        b = [points[2][0] - points[1][0], points[2][1] - points[1][1]]
        cos_ab = (a[0]*b[0] + a[1]*b[1]) / (sqrt(a[0]**2+a[1]**2) * sqrt(b[0]**2+b[1]**2))
        if abs(abs(cos_ab) - 1) < 0.0000001:
            return False
        else:
            return True

# @lc code=end

