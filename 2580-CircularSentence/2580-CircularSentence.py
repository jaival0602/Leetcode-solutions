# Last updated: 8/1/2025, 6:24:23 PM
class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sent = sentence.split(" ")
        n = len(sent)

        l_chr = sent[n-1][-1]
        for i in range(n):
            if sent[i][0] != l_chr:
                return False
            l_chr = sent[i][-1]
        
        return True

            