# Last updated: 8/1/2025, 6:26:47 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        res = 0 
        for i in range(1, n + 1): 
            count = 0
            for c in citations:
                if c >= i:
                    count += 1
            if count >= i:
                res = i 

        return res