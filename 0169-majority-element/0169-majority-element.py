class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k, count = 0, 0
        
        for num in nums:
            if count == 0:
                k = num
            count = count + 1 if num == k else count -1
        return k
        