# Last updated: 8/1/2025, 6:26:12 PM
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            n = (num[i] + k) // 10
            num[i] = (num[i]+ k) % 10
            k = n
        
        while k:
            n = k % 10
            k //= 10
            num = [n] + num
        return num
