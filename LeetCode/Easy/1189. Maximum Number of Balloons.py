class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """

        hm = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for c in text:
            if c in hm: hm[c] += 1
        
        ans = float('inf')
        for c in hm:
            if c == 'l' or c == 'o': ans = min(ans, int(hm[c]/2))
            else: ans = min(ans, hm[c])
        return ans
        
