# Last updated: 8/1/2025, 6:23:40 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        st = set()
        for x in nums:
            if x < k:
                return -1
            elif x > k:
                st.add(x)
        return len(st)