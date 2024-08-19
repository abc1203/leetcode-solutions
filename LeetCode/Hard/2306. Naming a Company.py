class Solution(object):
    def distinctNames(self, ideas):
        """
        :type ideas: List[str]
        :rtype: int

        idea:
         - capture the first letter in a dict (key=first letter, value=second letter)
         - for each set, find the number of common elements
         - add the uncommon elements to ans
         - Ex.
            a: a,b,c,d,e
            b: a,f,g,h,i
            {a} is the common element; if we replace the 1st letter, it'll always be in the other set
            so here it's 4x4=16
        """
        cnt = defaultdict(set)
        for idea in ideas:
            cnt[idea[0]].add(idea[1:])
        
        ans = 0
        possible_start = cnt.keys()
        for a in possible_start:
            for b in possible_start:
                common = len(cnt[a].intersection(cnt[b]))
                ans += (len(cnt[a])-common) * (len(cnt[b])-common)
        
        return ans


        
