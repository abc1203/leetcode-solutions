class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = s.lower()

        ans = 0
        for i in range(len(s)-1):
            if s[i] != s[i+1]: ans += 1
        return ans


        
