# Last updated: 8/1/2025, 6:24:37 PM
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        frequency = Counter(nums)
        return all(count % 2 == 0 for count in frequency.values())