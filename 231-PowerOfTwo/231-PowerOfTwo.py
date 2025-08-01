# Last updated: 8/1/2025, 6:28:57 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # log n = x log 2
        while n > 0:
            if n == 1:
                return True
            elif n % 2 == 0:
                n //= 2
            else:
                return False
        return False