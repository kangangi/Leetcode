class Solution:
    
    def reverse(self, nums: List[int], l: int, r: int) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
            
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        k = k % length
        left, right = 0, length - 1
        
        self.reverse(nums, left, right)
        self.reverse(nums, k, length-1)
        self.reverse(nums, 0, k-1)
        