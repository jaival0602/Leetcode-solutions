# Last updated: 8/1/2025, 6:23:50 PM
class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        n = len(word)
        curr = word[0]
        count = 1
        for i in range(1,n):
            if word[i] == curr:
                count += 1
                if count == 10:
                    ans += "9"+curr
                    count = 1
            else:
                if curr is not None:
                    ans += str(count) + curr
                curr = word[i]
                count = 1
        ans += str(count) + curr
        return ans