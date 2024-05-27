class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t): return False

        hm = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in hm: 
                if t[i] in used: return False
                hm[s[i]] = t[i]
                used.add(t[i])
            elif hm[s[i]] != t[i]: return False
        
        return True
        
