# Last updated: 8/1/2025, 6:26:38 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,int(num**0.5)+1):
            if i*i == num:
                return True
        else:
            return False