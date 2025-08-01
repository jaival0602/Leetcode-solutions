# Last updated: 8/1/2025, 6:26:22 PM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        pr_sum = 0
        sorted_pref_sum = 0

        for i in range(len(arr)):
            pr_sum += arr[i]
            sorted_pref_sum += i

            if pr_sum == sorted_pref_sum:
                chunks += 1
        
        return chunks