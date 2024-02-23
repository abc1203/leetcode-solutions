class Solution {
public:
    string add_bin(char a_digit, char b_digit, int carry) {
        int sum = a_digit - '0' + b_digit - '0' + carry;
        if(sum == 1 || sum == 3) {
            return "1";
        } else {
            return "0";
        }
    }

    int get_carry(char a_digit, char b_digit, int carry) {
        int sum = a_digit - '0' + b_digit - '0' + carry;
        if(sum < 2) {
            return 0;
        } else {
            return 1;
        }
    }

    string addBinary(string a, string b) {
        string ans = "";
        int a_pos = a.length() - 1; int b_pos = b.length() - 1;
        int carry = 0;

        while(a_pos >= 0 || b_pos >= 0 || carry == 1) {
            if(a_pos >= 0 && b_pos >= 0) {
                ans += add_bin(a[a_pos], b[b_pos], carry);
                carry = get_carry(a[a_pos], b[b_pos], carry);
                a_pos--; b_pos--;
            } else if(a_pos >= 0) {
                ans += add_bin(a[a_pos], '0', carry);
                carry = get_carry(a[a_pos], '0', carry);
                a_pos--;
            } else if(b_pos >= 0) {
                ans += add_bin('0', b[b_pos], carry);
                carry = get_carry('0', b[b_pos], carry);
                b_pos--;
            } else {
                ans += "1";
                carry = 0;
            }
        }
        
        string ans_rev;
        for(int i = ans.length()-1; i >= 0; i--) ans_rev += ans[i];
        return ans_rev;
    }
};
