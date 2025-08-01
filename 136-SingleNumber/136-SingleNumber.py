# Last updated: 8/1/2025, 6:27:43 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer ^= num
        return answer