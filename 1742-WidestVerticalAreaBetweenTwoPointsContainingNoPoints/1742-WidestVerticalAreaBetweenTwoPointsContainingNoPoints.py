# Last updated: 8/1/2025, 6:25:40 PM
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x_sorted = sorted([x for x, _ in points])

        max_width = 0
        for i in range(len(x_sorted) - 1):
            max_width = max(max_width, x_sorted[i + 1] - x_sorted[i])

        return max_width   