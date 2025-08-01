# Last updated: 8/1/2025, 6:24:26 PM
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        xor2 = 0
        len1 = len(nums1)
        len2 = len(nums2)

        if len2 % 2:
            for num in nums1:
                xor1 ^= num

        if len1 % 2:
            for num in nums2:
                xor2 ^= num

        return xor1 ^ xor2