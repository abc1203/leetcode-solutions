class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # sol 1:
        # l = s.split()
        # return len(l[-1])

        # sol 2:
        # ans, c = 0, 0
        # for i in range(len(s)):
        #     if s[i] != " ": c += 1
        #     else: 
        #         if c != 0: ans = c
        #         c = 0
        # return c if c != 0 else ans

        # sol 3:
        ans = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and ans != 0: return ans
            elif s[i] != " ": ans += 1
        return ans
        
