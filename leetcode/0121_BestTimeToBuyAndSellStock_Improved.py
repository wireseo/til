# knowledge: X
# concepts: Sliding Window
# comment: not as difficult as I thought it would be?
# runtime: X, not mine
# memory usage: X, not mine

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 # Buy pointer
        right = 1 # Sell pointer
        max_profit = 0
        
        while right < len(prices):
            if prices[left] < prices[right]:
                currentProfit = prices[right] - prices[left] # current profit
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
            
        return max_profit