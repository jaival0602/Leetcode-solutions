# Last updated: 8/1/2025, 6:26:23 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total = sum(nums)

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if right_sum == left_sum:
                return i
            
            left_sum += nums[i]
        
        return -1