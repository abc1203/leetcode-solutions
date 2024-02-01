class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        idea:
        dp[i] = min # of coins of getting value i using the given coins
        dp[i] = min(1 + dp[i - val] for all val in coins s.t. val <= i)
        """
        
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        coins.sort()
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j] > i: break
                dp[i] = min(dp[i], 1 + dp[i - coins[j]])
        
        if dp[amount] != amount+1: return dp[amount]
        return -1

        
