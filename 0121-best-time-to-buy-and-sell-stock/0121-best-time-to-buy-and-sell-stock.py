class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, buy = 0 , prices[0]
        
        for p in prices:
            max_profit = max(max_profit, p-buy)
            buy = min(buy, p)
            
        return max_profit