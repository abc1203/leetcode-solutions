class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool

        idea (DP):
         - dp[i][j] = you over opponent's score in piles[i:j+1]
             = piles[i] - dp[i+1][j] if you pick i (substract bc it's now opp)
             = piles[j] - dp[i][j-1] if you pick j 
        """
        return True
        dp = [[0] * (len(piles)+1) for _ in range(len(piles)+1)]

        for i in range(len(piles)): dp[i][i] = piles[i]

        for i in range(len(piles)):
            for j in range(len(piles)):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])
        
        return True if dp[0][len(piles)-1] >= 0 else False
