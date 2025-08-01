# Last updated: 8/1/2025, 6:24:11 PM
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary = set(dictionary)
        dp = dict()
        def dfs(i,j):
            nonlocal dictionary, dp, s
            if i>j:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            ans = dfs(i+1,j) + 1
            for k in range(i,j+1):
                if s[i:k+1] in dictionary:
                    ans = min(ans, dfs(k+1,j))
            dp[(i,j)] = ans
            return ans
        ans = dfs(0,len(s)-1)
        return ans