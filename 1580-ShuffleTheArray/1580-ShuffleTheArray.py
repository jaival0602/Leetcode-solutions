# Last updated: 8/1/2025, 6:25:48 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1 = []
        l2 = []
       
        for i in range (0, n):
            l1.append(nums[i])
            
            
        for j in range (n , 2*n):
            l2.append(nums[j])
            
            
        tot = []
        for k in range(0,n):
            tot.append(l1[k])
            tot.append(l2[k])
        return tot
            

        