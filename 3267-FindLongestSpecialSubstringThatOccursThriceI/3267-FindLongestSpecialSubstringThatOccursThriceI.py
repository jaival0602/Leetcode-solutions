# Last updated: 8/1/2025, 6:23:58 PM
class Solution:
    def maximumLength(self, s: str) -> int:
        count = {}
        for start in range(len(s)):
            curr_string = (
                []
            )  # Use a list to store the characters of the current substring
            for end in range(start, len(s)):
                if not curr_string or curr_string[-1] == s[end]:
                    curr_string.append(s[end])
                    curr_to_string = "".join(curr_string)  # Convert the list to a string
                    if curr_to_string in count:
                        count[curr_to_string] += 1
                    else:
                        count[curr_to_string] = 1
                else:
                    break
        ans = 0
        for str, freq in count.items():
            if freq >= 3 and len(str) > ans:
                ans = len(str)

        if ans == 0:
            return -1
        return ans