# Last updated: 8/1/2025, 6:23:55 PM
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = max_dec = max_len = 1
        n = len(nums)
        
        for i in range(n-1):
            if nums[i + 1] > nums[i]:
                max_inc += 1
                max_dec = 1
            elif nums[i + 1] < nums[i]:
                max_inc = 1
                max_dec += 1    
            else:
                max_inc = max_dec = 1
           
            max_len = max(max_len, max_inc, max_dec)

        return max_len

        
        