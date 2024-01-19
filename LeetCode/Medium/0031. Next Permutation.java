class Solution {
    public void nextPermutation(int[] nums) {
        // algorithm: 
        // start from last, find longest non-increasing suffix
        // set the one before to be the pivot
        // find the rightmost successor to swap with pivot; successor > pivot
        // reverse suffix

        int pivot = nums.length - 1;
        if(pivot == 0) return;
        while(pivot > 0 && nums[pivot] <= nums[pivot-1]) --pivot;
        --pivot;

        if(pivot != -1) {
            int id = nums.length - 1;
            while(id > pivot && nums[pivot] >= nums[id]) --id;
            int tmp = nums[pivot];
            nums[pivot] = nums[id];
            nums[id] = tmp;
        }

        for(int i = pivot+1; i < ((pivot+1)+nums.length)/2; ++i) {
            int tmp = nums[i];
            nums[i] = nums[nums.length + pivot - i];
            nums[nums.length + pivot - i] = tmp;
        }
    }
}

