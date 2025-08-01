# Last updated: 8/1/2025, 6:27:27 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 , rob2 = 0 , 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2