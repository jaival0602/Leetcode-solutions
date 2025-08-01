# Last updated: 8/1/2025, 6:27:39 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        
        for x in nums:
            count[x] += 1

        for x, freq in count.items():
            if freq == 1:
                return x
        
        return -1