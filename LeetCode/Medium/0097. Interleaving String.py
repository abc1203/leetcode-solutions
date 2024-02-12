class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool

        idea (dp):
         - dp[i][j] = whether s3[:i+j] can be formed by interleaving of s1[:i] and s2[:j]
         - dp[i][j] = (dp[i-1][j] and s3[i+j-1]==s1[i-1]) or (dp[i][j-1] and s3[i+j-1]==s2[j-1])
        """

        if len(s1) + len(s2) != len(s3): return False

        dp = [[False] * (len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0] = True

        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 and j == 0: continue
                elif i == 0: dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1])
                elif j == 0: dp[i][j] = (dp[i-1][j] and s3[i+j-1] == s1[i-1])
                else:
                    dp[i][j] = (dp[i][j-1] and s3[i+j-1] == s2[j-1]) or \
                                (dp[i-1][j] and s3[i+j-1] == s1[i-1])

        return dp[len(s1)][len(s2)]

        
