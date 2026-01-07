# Last updated: 1/7/2026, 9:37:49 AM
1class Solution:
2    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
3        count = 0
4        for i in nums:
5            if i %  2 == 0:
6                count |= i
7        return count