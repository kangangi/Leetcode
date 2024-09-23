class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        results = []
        for account in accounts:
            results.append(sum(account))
            
        return max(results)
        