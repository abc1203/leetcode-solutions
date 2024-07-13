class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        g.sort()
        s.sort()

        ans = 0
        i = 0
        for cSize in s:
            if i < len(g) and cSize >= g[i]: 
                ans += 1
                i += 1
        return ans

        
