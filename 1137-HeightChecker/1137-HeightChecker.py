# Last updated: 8/1/2025, 6:26:09 PM
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        ans = 0
        for i in range(len(expected)):
            if heights[i] != expected[i]:
                ans += 1
        return ans