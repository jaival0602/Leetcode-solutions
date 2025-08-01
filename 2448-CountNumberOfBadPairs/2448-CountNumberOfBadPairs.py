# Last updated: 8/1/2025, 6:24:32 PM
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pair = 0
        total_pair = 0
        count = defaultdict(int)
        for i in range(n):
            total_pair += i
            good_pair += count[nums[i] - i] 
            count[nums[i] - i] += 1
        return total_pair - good_pair