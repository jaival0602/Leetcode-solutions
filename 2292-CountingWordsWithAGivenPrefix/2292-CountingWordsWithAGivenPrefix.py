# Last updated: 8/1/2025, 6:24:38 PM
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.startswith(pref) for word in words)