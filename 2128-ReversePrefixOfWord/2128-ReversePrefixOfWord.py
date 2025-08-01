# Last updated: 8/1/2025, 6:24:46 PM
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result = list(word)
        left = 0

        for right in range(len(word)):
            # We found ch - reverse characters up to ch by swapping
            if result[right] == ch:
                while left < right:
                    result[right], result[left] = result[left], result[right]
                    left += 1
                    right -= 1
                return "".join(result)
        return word       