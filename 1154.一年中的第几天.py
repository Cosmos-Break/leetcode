#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
class Solution:
    def dayOfYear(self, data: str) -> int:
        year = int(data[0:4])
        month = int(data[5:7])
        day = int(data[8:])
        dic = [31,28,31,30,31,30,31,31,30,31,30,31]
        if year%400==0 or year%4==0 and year%100!=0:
            dic[1]=29
        return sum(dic[:month-1])+day
# @lc code=end

