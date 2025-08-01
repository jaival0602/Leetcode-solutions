# Last updated: 8/1/2025, 6:28:00 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Iterate from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9
        return [1] + digits






        # digits = map(str, digits)
        # digits = ''.join(digits)
        # digits = int(digits) + 1
        # digits = list[digits]
        # return digits

