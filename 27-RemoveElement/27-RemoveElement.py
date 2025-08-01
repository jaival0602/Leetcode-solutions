# Last updated: 8/1/2025, 6:28:10 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[idx] = nums[i]
                idx += 1
        return idx

### The idea is to traverse the nums and check for every element is equal to val
### If it is equal add count by 1 for the index and new value of nums[idx]
### return the index and the new arr
