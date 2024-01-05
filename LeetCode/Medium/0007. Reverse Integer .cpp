class Solution {
public:
    int reverse(int x) {
        bool isNegative  = false;
        
        if(-10 < x && x < 10) {
            return x;
        } else if (x == -2147483648) {
            return 0;
        }
        
        if(x < 0) { isNegative = true; }
        x = abs(x);
        
        string str = to_string(x);
        ::reverse(str.begin(), str.end());
        //cout << x << endl;
        //cout << str << endl;
        
        
        if(isNegative)  {
            if(stoi(str.substr(0, str.length()-1)) > INT_MAX/10 || 
               stoi(str.substr(0, str.length()-1)) == INT_MAX/10 && str[str.length()] > 8) {
                return 0;
            } else {
                return stoi(str)*(-1);
            }
        } else {
            if(stoi(str.substr(0, str.length()-1)) > INT_MAX/10 || 
               stoi(str.substr(0, str.length()-1)) == INT_MAX/10 && str[str.length()] > 7) {
                return 0;
            } else {
                return stoi(str);
            }
        }
    }
};
