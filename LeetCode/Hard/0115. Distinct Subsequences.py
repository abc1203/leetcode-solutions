class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int

        idea (dp):
         - dp[i][j] = # of distinct subseq where s[:i] == t[:j]
         - if s[i-1]==t[j-1], dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
             - if equal, there are 2 cases:
             1. use s[i-1] for t[j-1] => dp[i-1][j-1]
             2. don't use s[i-1] for t[j-1] => dp[i-1][j] (only case when not equal)
         - else dp[i][j] = dp[i-1][j]
        """

        dp = [[0] * (len(t)+1) for i in range(len(s)+1)]
        for i in range(len(dp)): dp[i][0] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[i])):
                if s[i-1] == t[j-1]: dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]
        
        return dp[len(s)][len(t)]
        
