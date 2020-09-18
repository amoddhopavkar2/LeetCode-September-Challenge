# Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        max_profit = 0
        low = prices[0]
        for i in range(1, n):
            low = min(low, prices[i])
            max_profit = max(max_profit, prices[i] - low)

        return max_profit
        