class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int

        idea (dp):
        dp[i][j] = len of longest common subseq for text1[:i] & text2[:j]
        if txt1[i] == txt2[j], dp[i][j] = dp[i-1][j-1]
        if not equal, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        """

        dp = [[0] * (len(text2)+1) for i in range(len(text1)+1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(text1)-1][len(text2)-1]
        
