# Last updated: 8/1/2025, 6:23:48 PM
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            if i%3 !=0:
                count+=1
        
        return count
        