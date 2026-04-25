class Solution {
    public int maximumDifference(int[] nums) {
        int a=nums[0];
        int b=-1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>a){
                b=Math.max(b,nums[i]-a);
            }
            else{
                a=nums[i];
            }
        }
        return b;
    }
}