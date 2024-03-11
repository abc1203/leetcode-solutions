class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]


    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]

        idea:
         - iterate(i) returns all such substr for s[i:]
         - it will check all ind s.t. i < ind < len(s) for the split:
             - only works if s[i:ind] is a palindrome first
             - then get all palindrome substr of s[ind:]
        """

        ans = []
        curr_substr = []

        def iterate(i):
            if i >= len(s):
                ans.append(list(curr_substr))
                return
            
            for ind in range(i+1, len(s)+1):
                if self.isPalindrome(s[i:ind]):
                    curr_substr.append(s[i:ind])
                    iterate(ind)
                    curr_substr.pop()
        
        iterate(0)
        return ans

        
