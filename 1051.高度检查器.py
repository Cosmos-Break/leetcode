#
# @lc app=leetcode.cn id=1051 lang=python3
#
# [1051] 高度检查器
#

# @lc code=start
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heights_ref = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != heights_ref[i]:
                res += 1
        return res

# @lc code=end

