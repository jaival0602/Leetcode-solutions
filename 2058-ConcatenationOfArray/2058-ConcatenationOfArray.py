# Last updated: 8/1/2025, 6:24:49 PM
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(2):
            for n in nums:
                ans.append(n)

        return ans