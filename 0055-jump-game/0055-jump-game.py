class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        n = len(nums) - 1
        for i in range(n):
            jumps = max(jumps, nums[i])

            if i < n  and not jumps:
                return False

            jumps -= 1
        
        return True
        