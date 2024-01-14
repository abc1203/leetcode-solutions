class Solution {
    public int removeDuplicates(int[] nums) {
        for(int i = 0; i < nums.length - 1; ++i) {
            // put j to be the 1st non-dupliate index after i
            int j = i + 1;
            while(nums[j] <= nums[i] && j < nums.length - 1) ++j;
            
            nums[i+1] = nums[j];
        }

        // find length of non-duplicate array
        if(nums.length == 1) return 1;
        for(int i = 0; i < nums.length - 1; ++i) {
            if(nums[i] == nums[i+1]) return i+1;
        }
        return nums.length;
    }
}
