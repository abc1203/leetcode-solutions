class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int

        idea (dp):
         - dp[i][j] = min # of ops to convert word1[:i] to word2[:j]
         - if word1[i-1]==word2[j-1], dp[i][j] = dp[i-1][j-1]
         - add a char => dp[i][j] = 1 + dp[i][j-1]
         - delete a char => dp[i][j] = 1 + dp[i-1][j]
         - replace a char => dp[i][j] = 1 + dp[i-1][j-1]
        """

        dp = [[0] * (len(word2)+1) for i in range(len(word1)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                if i == 0 and j == 0: continue
                elif j == 0: dp[i][j] = 1 + dp[i-1][j]
                elif i == 0: dp[i][j] = 1 + dp[i][j-1]
                else:
                    if word1[i-1] == word2[j-1]: dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])
        
        return dp[len(word1)][len(word2)]


        
