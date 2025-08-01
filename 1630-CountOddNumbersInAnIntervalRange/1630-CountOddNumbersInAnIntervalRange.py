# Last updated: 8/1/2025, 6:25:44 PM
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        length = high - low + 1
        count = length // 2
        if length % 2 and low % 2:
            count += 1
        return count 