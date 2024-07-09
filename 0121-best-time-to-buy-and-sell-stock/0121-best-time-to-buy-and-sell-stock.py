class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy =  0
        
        maximum_profit = 0
        
        for sell in range(1, len(prices)):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                maximum_profit = max(maximum_profit, profit)
            else:
                buy = sell
        return maximum_profit