class Solution {
public:
    bool isPalindrome(int x) {
        string reversed = to_string(x);
        reverse(reversed.begin(), reversed.end());
        
        if(to_string(x).compare(reversed) == 0) {
            return true;
        }
        return false;
    }
};
