class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        An misinterpretation of Leetcode 0322. Coin Change
        Finds the number of ways to get a certain amount using the given coin denominations
        dp[i] = # of ways of getting value i using the given coins
        dp[i] = dp[i - val] for all val in coins s.t. val <= i
        """
        
        dp = [0] * (amount+1)
        dp[0] = 1
        coins.sort()
        for i in range(amount+1):
            for j in range(len(coins)):
                if coins[j] > i: break
                dp[i] += dp[i - coins[j]]
            print(dp[i])
        
        if dp[amount] != 0 or amount == 0: return dp[amount]
        return -1

        
