# Last updated: 8/1/2025, 6:24:00 PM
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []
        for index, word in enumerate(words):
            if x in word:
                out.append(index)
        return out