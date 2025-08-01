// Last updated: 8/1/2025, 6:26:36 PM
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0; //intitialize count
        int result = 0; //initialize max
      
        for (int i=0 ; i < nums.length ; i++)
        {
              
            // Reset count when 0 is found
            if (nums[i] == 0)
                count = 0;
      
            // If 1 is found, increment count
            // and update result if count becomes
            // more.
            else
            {
                count++;//increase count
                result = Math.max(result, count);
            }
        }
      
        return result;
        
    }
}