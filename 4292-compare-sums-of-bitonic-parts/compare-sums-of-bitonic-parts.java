class Solution {
    public int compareBitonicSums(int[] nums) {

        int max=Integer.MIN_VALUE;

        for(int key:nums){
            if(key>max){
                max=key;
            }
        }

        long sum1=0;
        int index=-1;
        for(int i=0;i<nums.length;i++){
            sum1+=nums[i];
            if(nums[i]==max){
                index=i;
                break;
            }
        }

        long sum2=0;
        for(int i=index;i<nums.length;i++){
            sum2+=nums[i];
        }

        if(sum1>sum2){
            return 0;
        }
        else if(sum2>sum1){
            return 1;
        }
        return -1;

        
    }
}