class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        lis = s.split()
        if len(pattern) != len(lis): return False

        hm = {}
        for i in range(len(pattern)):
            if pattern[i] not in hm:
                if lis[i] not in hm.values(): hm[pattern[i]] = lis[i]
                else: return False
            elif hm[pattern[i]] != lis[i]: return False
        return True

        
