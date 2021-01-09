#
# @lc app=leetcode.cn id=135 lang=python3
#
# [135] 分发糖果
#

# @lc code=start
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1] and candys[i] <= candys[i - 1]:
                candys[i] = candys[i - 1] + 1
        for j in range(len(ratings) - 1, 0, -1):
            if ratings[j - 1] > ratings[j] and candys[j - 1] <= candys[j]:
                candys[j - 1] = candys[j] + 1
        return sum(candys)
# @lc code=end

