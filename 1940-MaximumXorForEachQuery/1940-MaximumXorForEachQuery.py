# Last updated: 8/1/2025, 6:25:25 PM
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        answer = []
        max_k = (1 << maximumBit) - 1 
        current_xor = 0
        
        for num in nums:
            current_xor ^= num
    
        for i in range(len(nums)):
            k = current_xor ^ max_k
            answer.append(k)            
            current_xor ^= nums[len(nums) - 1 - i]
        
        return answer
