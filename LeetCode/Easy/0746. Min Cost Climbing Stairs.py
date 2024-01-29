class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int

        dp[i] = min cost for going on the ith step
        dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        """

        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1] + cost[i], dp[i-2] + cost[i])
        
        return min(dp[len(cost)-1], dp[len(cost)-2])
        
