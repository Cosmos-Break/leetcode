#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0
        intervals = sorted(intervals, key=lambda interval: interval[-1])
        print(intervals)
        need_remove = 0
        j = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[j][-1]:
                j = i
                continue
            else:
                need_remove += 1
        return need_remove
            
# @lc code=end

