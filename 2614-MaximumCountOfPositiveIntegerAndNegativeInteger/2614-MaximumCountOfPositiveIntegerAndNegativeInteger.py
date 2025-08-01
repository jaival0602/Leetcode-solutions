# Last updated: 8/1/2025, 6:24:19 PM
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = neg = 0

        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1

        return max(pos,neg)