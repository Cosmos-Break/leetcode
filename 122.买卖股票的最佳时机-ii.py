#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        lowest_price = prices[0]
        current_profit = 0
        for price in prices[1:]:
            if price < lowest_price:
                lowest_price = price
            else:
                current_profit += price - lowest_price
                lowest_price = price
        return current_profit

# @lc code=end

