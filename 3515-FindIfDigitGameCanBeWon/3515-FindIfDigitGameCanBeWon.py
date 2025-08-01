# Last updated: 8/1/2025, 6:23:45 PM
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = 0
        d = 0
        for i in nums:
            if len(str(i)) == 1:
                s += i
            else:
                d += i
        return s != d