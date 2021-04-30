#
# @lc app=leetcode.cn id=888 lang=python3
#
# [888] 公平的糖果棒交换
#

# @lc code=start
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        set_b = set(B)
        diff = (sum(A) - sum(B)) // 2
        for a in A:
            if a-diff in set_b:
                return [a, a-diff]
            
# @lc code=end

