# Last updated: 8/1/2025, 6:25:31 PM
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre = max_pre = res = cur = 0

        for n in nums:
            cur += n
            res = max(res, abs(cur - min_pre), abs(cur - max_pre))
            min_pre = min(cur, min_pre)
            max_pre = max(cur, max_pre)
        return res