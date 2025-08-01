# Last updated: 8/1/2025, 6:24:28 PM
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, cnt = 0, 0
        
        max_element = max(nums)
        for num in nums:
            if num == max_element:
                cnt += 1
            else:
                cnt = 0
            ans = max(ans, cnt)
        return ans