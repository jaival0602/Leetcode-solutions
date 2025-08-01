# Last updated: 8/1/2025, 6:26:20 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        new_str = s + s

        return new_str.find(goal) != -1