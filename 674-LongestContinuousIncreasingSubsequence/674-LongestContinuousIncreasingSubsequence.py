# Last updated: 8/1/2025, 6:26:24 PM
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 0
        longest = 0

        for i in range(len(nums)):
            if nums[i] > nums[i-1]:
                longest += 1
            else:
                longest = 1

            res = max(res, longest)
        
        return res