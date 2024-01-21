class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str

        idea:
        use sliding window with l & r
        if l & r forms a window substr, increment l until it reaches a char that's in t
        whenever we reach a new value of l, check if the new l & r still forms a window substr; if it still does, continue incrementing l 
        """

        ans = ""
        l = 0
        mp = {}
        for r in range(len(t)):
            mp[t[r]] = 1 + mp.get(t[r], 0)
        
        for r in range(len(s)):
            if s[r] in mp:
                mp[s[r]] -= 1
                
                while all(count <= 0 for count in mp.values()):
                    if ans == "" or (r - l + 1) < len(ans):
                        ans = s[l:r+1]
                    
                    if s[l] in mp: mp[s[l]] += 1
                    while True: 
                        l += 1
                        if l == len(s) or s[l] in mp: break
        
        return ans



        
