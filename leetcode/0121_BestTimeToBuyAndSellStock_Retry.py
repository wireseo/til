class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0] 
        profit, maxProfit = 0, 0
        
        for sell in prices:
            if sell < buy: # update new buying price
                buy = sell
            profit = sell - buy
            maxProfit = max(profit, maxProfit) 
                
        return maxProfit