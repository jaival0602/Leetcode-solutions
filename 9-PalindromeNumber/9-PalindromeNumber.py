# Last updated: 8/1/2025, 6:28:17 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y = str(x)[::-1]
        if x==y:
            return True
