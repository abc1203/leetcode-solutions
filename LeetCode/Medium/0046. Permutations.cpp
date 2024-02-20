class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        int curr = nums[0];
        if(nums.size() == 1) {
            vector<int> one_perm = {curr};
            ans.push_back(one_perm);
            return ans;
        }

        vector<int> new_nums;
        for(int i = 1; i < nums.size(); i++) new_nums.push_back(nums[i]);
        vector<vector<int>> old_perm = permute(new_nums);

        for(int i = 0; i < old_perm.size(); i++) {
            for(int j = 0; j <= old_perm[i].size(); j++) {
                vector<int> one_perm = old_perm[i];
                one_perm.insert(one_perm.begin() + j, curr);
                ans.push_back(one_perm);
            }
        }
        return ans;
    }
};
