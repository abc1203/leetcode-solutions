class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool

        idea:
        use pointers l & r; we access whether if letters between l & r form a permutation for s1
        once we determined that the letters between l & r cannot be a permutation, we increment l until s2[l] == s2[r] and add 1
        => new l will have s2[l-1] == s2[r]
        """

        mp = {}
        char_set = set(s1)
        for i in range(len(s1)):
            if s1[i] in mp:
                mp[s1[i]] += 1
            else:
                mp[s1[i]] = 1

        l = 0
        for r in range(len(s2)):
            if s2[r] not in mp:
                i = l
                while s2[l] != s2[r]: l += 1
                l += 1

                while i < len(s2) and i < l:
                    if s2[i] in char_set:
                        if s2[i] in mp:
                            mp[s2[i]] += 1
                        else:
                            mp[s2[i]] = 1
                    i += 1
                
            if s2[r] in mp:
                mp[s2[r]] -= 1
                if mp[s2[r]] == 0: del mp[s2[r]]

            if len(mp) == 0: return True             
        
        return False
