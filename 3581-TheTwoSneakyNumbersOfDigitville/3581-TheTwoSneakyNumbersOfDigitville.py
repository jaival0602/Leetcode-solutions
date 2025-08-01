# Last updated: 8/1/2025, 6:23:43 PM
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        seen = set()
        for x in nums: 
            if x in seen: ans.append(x)
            else: seen.add(x)
        return ans 