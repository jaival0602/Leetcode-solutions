# Last updated: 8/1/2025, 6:28:58 PM
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            part_start_index = s.find(part)
            s = s[:part_start_index] + s[part_start_index + len(part) :]
        return s