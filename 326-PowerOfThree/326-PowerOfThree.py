# Last updated: 8/1/2025, 6:26:41 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n%3==0:
            n//=3
        return n==1