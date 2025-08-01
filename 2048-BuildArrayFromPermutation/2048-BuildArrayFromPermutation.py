# Last updated: 8/1/2025, 6:24:50 PM
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])

        return ans