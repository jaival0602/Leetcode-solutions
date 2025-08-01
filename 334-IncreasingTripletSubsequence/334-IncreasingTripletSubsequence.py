# Last updated: 8/1/2025, 6:26:40 PM
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False