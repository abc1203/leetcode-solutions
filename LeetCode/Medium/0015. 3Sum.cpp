class Solution {
public:
    
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res; 
        int idx1, idx2;
        if(nums.size() < 3) return res;
        
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < nums.size()-2; i++) {
            if(i != 0 && nums[i] == nums[i-1]) continue;
            idx1 = i + 1; idx2 = nums.size()-1;
            
            while(idx1 < idx2) {
                if(idx1 != i+1 && nums[idx1] == nums[idx1-1]) {
                    idx1++; continue;
                } else if(idx2 != nums.size()-1 && nums[idx2] == nums[idx2+1]) {
                    idx2--; continue;
                }
                
                int sum = nums[i] + nums[idx1] + nums[idx2];
                
                if(sum == 0) {
                    vector<int> triplet = {nums[i], nums[idx1], nums[idx2]};
                    res.push_back(triplet);
                    idx2--;
                } else if(sum < 0) {
                    idx1++;
                } else if(sum > 0) {
                    idx2--;
                }
            }
        }
        
        return res;
        
    }
};
