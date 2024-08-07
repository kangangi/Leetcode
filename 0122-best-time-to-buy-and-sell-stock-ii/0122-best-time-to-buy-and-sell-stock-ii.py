class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        no_stock = 0
        has_stock = -prices[0]
        
        for price in prices[1:]:
            new_no_stock = max(no_stock, has_stock + price)
            new_has_stock = max(has_stock, no_stock - price)
            no_stock, has_stock = new_no_stock, new_has_stock
        
        return no_stock