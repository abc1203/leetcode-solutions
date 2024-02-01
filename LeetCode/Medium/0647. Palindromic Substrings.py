class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int

        idea (dp O(n^2)):
         - for every index i in s, check all the palindromes starting in that pos
             - both even & odd len should be checked
             - O(1) for each check
        """

        ans = 0
        n = len(s)
        for i in range(len(s)):
            # odd len
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
            
            # even len
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1
        
        return ans
        
