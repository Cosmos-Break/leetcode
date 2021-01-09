#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
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
                current_profit = price - lowest_price
            if max_profit < current_profit:
                max_profit = current_profit
        return max_profit
            
# @lc code=end

