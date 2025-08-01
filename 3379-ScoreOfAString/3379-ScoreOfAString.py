# Last updated: 8/1/2025, 6:23:54 PM
class Solution:
    def scoreOfString(self, s: str) -> int:
        count = 0
        for i in range(1,len(s)):
            count = count + abs(ord(s[i-1])-ord(s[i]))
        return count
