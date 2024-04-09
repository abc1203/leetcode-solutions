class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int

        idea:
         - run longest common subseq algo on s and s[::-1]
         - longest common subseq:
             - dp[i][j] = length of longest common subseq for s1[:i] and s2[:j]
                 = dp[i-1][j-1] + 1 if s1[i] == s2[j]
                 = max(dp[i-1][j], dp[i][j-1]) elsewise
        """

        def longestCommonSubseq(s1, s2):
            dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]

            for i in range(len(s1)):
                for j in range(len(s2)):
                    if s1[i] == s2[j]:
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            return dp[len(s1)-1][len(s2)-1]
        
        return longestCommonSubseq(s, s[::-1])

        
