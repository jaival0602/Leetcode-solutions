# Last updated: 8/1/2025, 6:28:55 PM
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]

        return ""