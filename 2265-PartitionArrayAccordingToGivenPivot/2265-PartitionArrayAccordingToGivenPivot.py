# Last updated: 8/1/2025, 6:24:39 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less = []
        equal = []
        greater = []

        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                equal.append(num)

        less.extend(equal)
        less.extend(greater)

        return less