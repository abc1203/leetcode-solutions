class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        idea (dp):
        at ith iteration, check if s[:i] can be satisfied by wordDict
        """

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i - len(word) >= 0 and s[i - len(word):i] == word:
                    dp[i] = dp[i - len(word)]
                if dp[i]: break
        
        return dp[len(s)]
        
