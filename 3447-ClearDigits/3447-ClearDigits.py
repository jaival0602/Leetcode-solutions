# Last updated: 8/1/2025, 6:23:50 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        s = list(s)
        char_index = 0

        while char_index < len(s):
            if s[char_index].isdigit():
                del s[char_index]
                if char_index > 0:
                    del s[char_index - 1]
                    char_index -= 1
            else:
                char_index += 1
        return "".join(s)