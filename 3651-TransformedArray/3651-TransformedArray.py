# Last updated: 2/5/2026, 5:41:46 PM
class Solution:
    def constructTransformedArray(self, nums):
        n = len(nums)
        return [nums[((i + nums[i]) % n + n) % n] for i in range(n)]