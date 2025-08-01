# Last updated: 8/1/2025, 6:25:58 PM
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_digit_count = 0

        for num in nums:
            # Convert num to string and find its length
            length = len(str(num))
            if length % 2 == 0:
                even_digit_count += 1

        return even_digit_count