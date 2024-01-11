class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int sum, closestSum, minDiff = INT_MAX;
        int idx1, idx2;
        
        for(int i = 0; i < nums.size(); i++) {
            idx1 = i+1; idx2 = nums.size()-1;
            
            while(idx1 < idx2) {
                sum = nums[i] + nums[idx1] + nums[idx2];
                
                if(sum == target) {
                    return sum;
                } else {
                    if(abs(sum - target) < minDiff) {
                        closestSum = sum; 
                        minDiff = abs(sum - target);
                    }
                    
                    if(sum < target) {
                        idx1++;
                    } else {
                        idx2--;
                    }
                }
            }
        }
        
        return closestSum;
    }
};
