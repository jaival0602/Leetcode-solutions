# Last updated: 8/1/2025, 6:27:25 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def num_sq(n):
            res = 0

            while n:
                digit = n%10
                res = res + digit**2
                n = n // 10

            return res

        while n not in visit:
            visit.add(n)
            n = num_sq(n)
            if n == 1:
                return True
        
        return False