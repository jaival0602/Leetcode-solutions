# Last updated: 8/1/2025, 6:26:33 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
        
            res = max(count, res)
        return res
