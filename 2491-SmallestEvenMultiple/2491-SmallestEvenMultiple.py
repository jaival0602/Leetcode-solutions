# Last updated: 8/1/2025, 6:24:29 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        c = n
        while c % n or c % 2 :
            c += 1
        return c