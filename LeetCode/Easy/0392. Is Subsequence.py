class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        approach: O(min(chars in t to get s, |t|))
         - check if t can satisfy all indices of s
        """

        i, j = 0, 0
        while i < len(s):
            if j == len(t): return False
            if s[i] == t[j]: i += 1
            j += 1
        
        return True
        
