class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, max_count = 0, 0
        
        for i in nums:
            if i == 1:
                count += 1
                max_count = count if count > max_count else max_count
            else:
                count = 0
                
        return max_count
        