# Last updated: 8/1/2025, 6:23:41 PM
class Solution:
    def isBalanced(self, num: str) -> bool:
        even_sum = odd_sum = 0
    
        for i in range(0, len(num), 2):
            even_sum += int(num[i])
    
        for i in range(1, len(num), 2):
            odd_sum += int(num[i])
    
        return even_sum == odd_sum