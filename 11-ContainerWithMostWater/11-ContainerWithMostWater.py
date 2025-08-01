# Last updated: 8/1/2025, 6:28:17 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i = 0
        j = n-1
        max_amount = min(height[i],height[j])*(j-i)
        while i<j:
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
            volume = min(height[i],height[j])*(j-i)
            max_amount = max(max_amount, volume)
        return max_amount
