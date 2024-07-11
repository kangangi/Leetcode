class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k, count = 0, 0
        
        for num in nums:
            if count == 0:
                k = num
            count +=  1 if num == k else -1
        return k
        