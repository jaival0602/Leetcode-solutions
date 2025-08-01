# Last updated: 8/1/2025, 6:25:56 PM
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        curr = 0
        d = [curr]
        for i in range(n):
            curr ^= arr[i]
            d.append(curr)
        ans = []
        for query in queries:
            ans.append(d[query[1]+1]^d[query[0]])
        return ans