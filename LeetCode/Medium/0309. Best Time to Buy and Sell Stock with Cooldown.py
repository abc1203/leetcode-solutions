class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        idea (dp):
        dp[i][buy] = profit at the ith item with the decision to buy or not
         - i is the ith item, buy is whether to buy (to buy == 1)
        to buy => need to check the next day => i+1
        to sell => need to check the day after next => i+2
        """

        dp = [[0] * (2) for i in range(len(prices)+2)]

        for i in range(len(prices)-1, -1, -1):
            for to_buy in range(2):
                if to_buy == 1: 
                    dp[i][1] = max(dp[i+1][0] - prices[i], dp[i+1][1])
                else:
                    dp[i][0] = max(dp[i+2][1] + prices[i], dp[i+1][0])
        
        return dp[0][1]
        
