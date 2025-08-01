# Last updated: 8/1/2025, 6:26:30 PM
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h = time[:2]
            m = time[3:]
            minutes.append(int(h)*60 + int(m))

        minutes.sort()
        ans = 24*60
        for i in range(len(minutes)-1):
            ans = min(ans, minutes[i+1] - minutes[i])
        return min(ans, 24*60 - minutes[len(minutes)-1] + minutes[0])