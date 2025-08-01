# Last updated: 8/1/2025, 6:24:44 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        max_diff = -1
        
        for right in range(1, n):
            if nums[right] > nums[left]:
                max_diff = max(max_diff, nums[right] - nums[left])
            else:
                left = right  
        
        return max_diff

