# Last updated: 8/1/2025, 6:25:53 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for i in range (len(candies)):
            if max_candy <= candies[i] + extraCandies:
                result.append(True)
            else:
                result.append(False)
        return result

