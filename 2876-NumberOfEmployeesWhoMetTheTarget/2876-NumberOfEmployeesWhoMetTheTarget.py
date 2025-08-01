# Last updated: 8/1/2025, 6:24:07 PM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                res += 1
        return res