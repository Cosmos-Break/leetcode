#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    # TLE:
    # def maxArea(self, height: List[int]) -> int:
    #     max_area = 0
    #     n = len(height)
    #     for i in range(n):
    #         for j in range(i, n):
    #             area = (j - i) * min(height[i], height[j])
    #             max_area = max(max_area, area)
    #     return max_area

    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        n = len(height)
        i, j = 0, n - 1
        while i < j:
            if height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            else:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1
        return max_area

# @lc code=end

