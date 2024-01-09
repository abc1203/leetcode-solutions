class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        vector<int> result;
        int n1, n2;
        
        // check if target reached & insert into hashmap
        for(int i = 0; i < nums.size(); i++) {
            if(mp.find(nums[i]) != mp.end()) {
                n1 = nums[i];
                n2 = target - nums[i];
                break;
            }
            mp[target-nums[i]] = nums[i];
        }

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] == n1 || nums[i] == n2) {
                result.push_back(i);
            }
        }

        return result;
    }
};
