// Last updated: 8/1/2025, 6:26:00 PM
class Solution {
    public int findNumbers(int[] nums) {
        int count = 0;
        if(nums.length!=0){
            String strNum;
            for (int i=0; i < nums.length;i++){
                strNum = Integer.toString(nums[i]);
                if (strNum.length() % 2 ==0)
                    count++;
            }
        }
        return count;
    }
}