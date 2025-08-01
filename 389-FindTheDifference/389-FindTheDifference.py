# Last updated: 8/1/2025, 6:26:35 PM
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum = sum(ord(x) for x in s)
        t_sum = sum(ord(y) for y in t)
    
        return chr(t_sum - s_sum)