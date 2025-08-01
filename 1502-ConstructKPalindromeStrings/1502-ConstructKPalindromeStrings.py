# Last updated: 8/1/2025, 6:25:52 PM
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        freq = [0] * 26
        odd_cnt = 0

        for char in s:
            freq[ord(char) - ord("a")] += 1

        for count in freq:
            if count % 2 == 1:
                odd_cnt += 1

        return odd_cnt <= k



