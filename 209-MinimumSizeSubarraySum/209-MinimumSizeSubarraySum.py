# Last updated: 8/1/2025, 6:27:23 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum_cur = 0
        res = float("inf")
    
        for r in range(len(nums)):
            sum_cur += nums[r]

            while sum_cur >= target:
                res = min(res, r - l + 1)
                sum_cur -= nums[l]
                l += 1

        return res if res != float("inf") else 0
