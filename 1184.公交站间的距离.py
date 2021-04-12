#
# @lc app=leetcode.cn id=1184 lang=python3
#
# [1184] 公交站间的距离
#

# @lc code=start
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        pos_dis = sum(distance[start:destination])
        neg_dis = sum(distance) - pos_dis
        return min(pos_dis, neg_dis)

# @lc code=end

