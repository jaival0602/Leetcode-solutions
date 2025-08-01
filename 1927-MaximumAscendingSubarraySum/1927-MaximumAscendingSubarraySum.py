# Last updated: 8/1/2025, 6:25:21 PM
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        cur = nums[0]
        res = cur

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                cur += nums[i]
            else:
                cur = nums[i]
            res = max(res, cur)

        return res