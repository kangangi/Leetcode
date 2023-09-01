class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            num_digits = len(str(i))
            if num_digits % 2 == 0:
                count += 1
                
                
        return count
        