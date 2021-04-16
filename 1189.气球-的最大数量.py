#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count(key)//num for key,num in collections.Counter('balloon').items()) 

# @lc code=end

