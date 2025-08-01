# Last updated: 8/1/2025, 6:26:25 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        L,R = 0,k
        n = len(nums)
        main_sum = curr_sum = sum(nums[L:R])
        while R<n:
            curr_sum += (nums[R]- nums[L])
            main_sum = max(main_sum,curr_sum)
            L += 1
            R += 1
        return (main_sum/k)