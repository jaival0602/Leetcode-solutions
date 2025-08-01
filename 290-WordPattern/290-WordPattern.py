# Last updated: 8/1/2025, 6:26:45 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = list(s.split(" "))
        
        if len(pattern) != len(s):
            return False

        pattern_2_word ={}
        word_2_pattern = {}

        for p, w in zip(pattern, s):

            if pattern_2_word.get(p) and pattern_2_word[p] != w:
                return False
            
            if word_2_pattern.get(w) and word_2_pattern[w] != p:
                return False

            pattern_2_word[p] = w
            word_2_pattern[w] = p

        return True
            