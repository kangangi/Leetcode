class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        data = defaultdict(int)
        threshold = len(nums) / 2
        for i in nums:
            data[i] += 1
            if data[i] > threshold:
                return i
        