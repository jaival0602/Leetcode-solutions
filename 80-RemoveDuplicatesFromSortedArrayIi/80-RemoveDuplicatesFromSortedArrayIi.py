# Last updated: 8/1/2025, 6:27:56 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = {}
        k = 0

        for num in nums:
            count[num] = count.get(num,0) + 1
            if count[num] <= 2:
                nums[k] = num
                k += 1
        
        return k

# Create a dict to count of each element
# If the count is greater then 2 then remove it
# Increase the count by 1 and return the length of the array