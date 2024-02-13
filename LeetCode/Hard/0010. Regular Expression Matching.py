class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        idea (dp):
         - dp[i][j] = whether s[:i] matches p[:j]
         - if p[j-1] is a char, dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
         - if p[j-1] is '.', dp[i][j] = dp[i-1][j-1]
         - if p[j-1] is '*':
            case 1: '*' is zero elem => dp[i][j] = dp[i][j-2]
            case 2: '*' is one elem => dp[i][j] = dp[i-1][j-2] and s[i-1] == p[j-2]
            case 3: '*' is n elem => dp[i][j] = dp[i-n][j-2] and s[i-x] == p[j-2]
                    for x in range(2, n)
        """

        dp = [[False] * (len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True

        for i in range(len(dp)):
            for j in range(1, len(dp[i])):
                if p[j-1] == "*":
                    dp[i][j] = dp[i][j-2]

                    x = 1
                    while x <= i and (s[i-x] == p[j-2] or p[j-2] == "."):
                        dp[i][j] = dp[i][j] or dp[i-x][j-2]
                        x += 1
                        if dp[i][j] == True: break
                elif p[j-1] == ".": dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1]==p[j-1]

        return dp[len(s)][len(p)]



