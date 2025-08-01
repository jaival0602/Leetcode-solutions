# Last updated: 8/1/2025, 6:27:59 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]