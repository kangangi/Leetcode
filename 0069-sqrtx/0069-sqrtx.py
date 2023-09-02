import math

class Solution:
    def mySqrt(self, x: int) -> int:
        
        root = math.sqrt(x)
        return math.floor(root)