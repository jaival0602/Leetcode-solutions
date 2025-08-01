# Last updated: 8/1/2025, 6:26:02 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        counts = list(freq.values())
        return len(counts) == len(set(counts))