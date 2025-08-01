// Last updated: 8/1/2025, 6:26:13 PM
class Solution {
    public int[] sortedSquares(int[] nums) {
         for (int i = 0; i < nums.length; i++)
            nums[i] = nums[i] * nums[i];
        
        Arrays.sort(nums);
   
         return nums;
    }
   
}