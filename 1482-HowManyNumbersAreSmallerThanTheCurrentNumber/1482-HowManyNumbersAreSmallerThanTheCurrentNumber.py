# Last updated: 8/1/2025, 6:25:54 PM
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final=[]
        for i in range(0,len(nums)):
            count=0
            for j in range(0,len(nums)):
                if (i!=j and nums[j]<nums[i]):
                    count=count+1
                    
            
            
            final.append(count)
        return final
        