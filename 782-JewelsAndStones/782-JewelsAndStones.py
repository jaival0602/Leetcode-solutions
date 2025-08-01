# Last updated: 8/1/2025, 6:26:20 PM
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)  
        count = 0
        
        for stone in stones:
            if stone in jewel_set:
                count += 1
                
        return count