class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        dp[i][j] = longest palin subsequence in s[i:j] inc.
        if s[i] == s[j], dp[i][j] = 1 + dp[i+1][j-1]
        else, dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        """

        dp = [[0]*len(s) for i in range(len(s))]

        for i in range(len(dp)): dp[i][i] = 1

        for i in range(len(dp)-2, -1, -1):
            for j in range(i+1, len(dp[0])):
                if s[i] == s[j]: 
                    if j-i >= 2: dp[i][j] = 2 + dp[i+1][j-1]
                    else: dp[i][j] = 1 + dp[i][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][len(s)-1]



        
