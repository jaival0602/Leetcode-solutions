# Last updated: 8/1/2025, 6:28:02 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()

        return len(words[-1])