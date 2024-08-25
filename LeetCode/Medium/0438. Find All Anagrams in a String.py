class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        cnt_p = {}
        for c in p: cnt_p[c] = cnt_p.get(c, 0) + 1

        cnt_s = {}
        for i in range(len(s)):
            cnt_s[s[i]] = cnt_s.get(s[i], 0) + 1
            
            if i >= len(p): 
                to_del = i-len(p)
                cnt_s[s[to_del]] -= 1
                if cnt_s[s[to_del]] == 0: del cnt_s[s[to_del]]
            if cnt_p == cnt_s: ans.append(i-len(p)+1)
        return ans


        
        
