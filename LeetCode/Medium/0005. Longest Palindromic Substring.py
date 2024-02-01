class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        idea (dp O(n^2)):
         - if s[l:r] is a palindrome, check if s[l-1:r+1] is palindrome in O(1)
             - this is the subproblem structure
         - for each index of s, find the biggest possible palindrome
             - consider both even & odd cases
        """

        ans = ""
        n = len(s)
        for i in range(n):
            # odd (start on s[i])
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(ans): ans = s[l : r+1]
                l -= 1
                r += 1
            
            # even (start on s[i], s[i+1])
            l, r = i, i+1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1) > len(ans): ans = s[l : r+1]
                l -= 1
                r += 1
        
        return ans
        
