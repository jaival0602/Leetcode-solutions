# Last updated: 8/1/2025, 6:24:10 PM
class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        XOR = 0
        for element in derived:
            XOR = XOR ^ element
        return XOR == 0       