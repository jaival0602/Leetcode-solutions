# Last updated: 8/1/2025, 6:26:32 PM
import math
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(math.sqrt(area)), 1, -1):
            if area % i == 0:
                return [area//i,i]
        return [area, 1] 