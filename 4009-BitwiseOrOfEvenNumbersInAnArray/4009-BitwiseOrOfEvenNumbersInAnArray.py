# Last updated: 1/12/2026, 7:01:20 PM
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if i %  2 == 0:
                count |= i
        return count