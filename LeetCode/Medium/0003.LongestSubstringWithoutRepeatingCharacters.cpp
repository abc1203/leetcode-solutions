class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map;
        int ans = 0; int len = s.length();
        
        for(int j = 0, i = 0; j < len; ++j) {
            if(map.find(s[j]) != map.end()) {
                i = max(i, map.at(s[j]));
            }
            
            ans = max(ans, j - i + 1);
            map[s[j]] = j + 1;
        } 
        
        return ans;
    }
};
