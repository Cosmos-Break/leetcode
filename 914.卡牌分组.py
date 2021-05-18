#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        vals = collections.Counter(deck).values()
        return reduce(gcd, vals) >= 2

# @lc code=end

