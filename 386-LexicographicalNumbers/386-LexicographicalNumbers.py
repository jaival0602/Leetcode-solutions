# Last updated: 8/1/2025, 6:26:37 PM
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        # s = [str(i) for i in range(1,n+1)]
        # s.sort()
        # return list(map(int,s))
        ans = []
        def dfs(curr):
            nonlocal ans
            ans.append(curr)
            if curr*10>n:
                return
            else:
                curr = curr*10
                for num in range(10):
                    if curr+num<=n:
                        dfs(curr+num)
        for num in range(1,10):
            if num<=n:
                dfs(num)
        return ans