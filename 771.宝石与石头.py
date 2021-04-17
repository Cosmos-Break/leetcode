# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelsSet = set(jewels)
        a = (s in jewelsSet for s in stones)
        return sum(s in jewelsSet for s in stones)
# @lc code=end

