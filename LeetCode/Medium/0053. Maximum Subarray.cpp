class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size());
        int max_val = dp[0] = nums[0];
        
        for(int i = 1; i < dp.size(); i++) {
            dp[i] = max(nums[i], dp[i-1] + nums[i]);
            if(max_val < dp[i]) max_val = dp[i];
        }
        return max_val;
    }
};
