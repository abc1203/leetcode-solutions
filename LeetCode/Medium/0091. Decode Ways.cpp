class Solution {
public:
    int numDecodings(string s) {
        // idea (dp): dp[i] = # of ways to decode from s.substr(0, i)
        // case 1 (s[i] is 1-9): added a new char to dp[i-1] => dp[i] += dp[i-1]
        // case 2 (s[i-1] is 1 && s[i] is 0-9): dp[i] += dp[i-2]
        // case 3 (s[i-1] is 2 && s[i] is 0-6): dp[i] += dp[i-2]

        if(s[0] == '0') return 0;
        vector<int> dp(s.length() + 1);
        dp[0] = 1; dp[1] = 1;

        for(int i = 2; i <= s.length(); i++) {
            if(stoi(s.substr(i - 1, 1)) >= 1 && stoi(s.substr(i - 1, 1)) <= 9) {
                dp[i] += dp[i-1];
            }
            if(stoi(s.substr(i - 2, 2)) >= 10 && stoi(s.substr(i - 2, 2)) <= 26) {
                dp[i] += dp[i-2]; 
            }
            
        }
        return dp[s.length()];
    }
};
