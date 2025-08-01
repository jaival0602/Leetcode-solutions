# Last updated: 8/1/2025, 6:25:45 PM
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # n = len(arr)
        # pairs = 0
        
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if (arr[i] + arr[j]) % k == 0:
        #             print(arr[i],arr[j])
        #             pairs += 1
                
  
        #             if n // 2 == pairs:
        #                 return True
        # print(pairs)
        # return False
        n = len(arr)
        mods = [0]*k
        for i in range(n):
            mods[arr[i]%k] += 1
        count = mods[0]//2
        for i in range(1,k):
            j = k-i
            if i>j:
                break
            if i == j:
                count += mods[i]//2
            else:
                count += min(mods[i],mods[j])
        return count == n//2