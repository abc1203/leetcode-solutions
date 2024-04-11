class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        hmap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0

        i = 0
        while i < len(s):
            if i+1 < len(s) and hmap[s[i]] < hmap[s[i+1]]:
                ans = ans - hmap[s[i]] + hmap[s[i+1]]
                i += 2
            else:
                ans += hmap[s[i]]
                i += 1
        
        return ans


        
