class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int

        idea:
        dp[i] = min cost from start to ith day
             = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
        """

        dp = [0] * len(days)
        one_min_cost = min(costs)
        dp[0] = one_min_cost

        for i in range(1, len(days)):
            # cost for 1-day
            dp[i] = dp[i-1] + costs[0]

            # cost for 7-day
            curr_index = i - 1
            while curr_index >= 0 and days[i] - 7 < days[curr_index]:
                curr_index -= 1
            prev = dp[curr_index] if curr_index != -1 else 0
            dp[i] = min(dp[i], prev + costs[1])

            # cost for 30-day
            curr_index = i - 1
            while curr_index >= 0 and days[i] - 30 < days[curr_index]:
                curr_index -= 1
            prev = dp[curr_index] if curr_index != -1 else 0
            dp[i] = min(dp[i], prev + costs[2])
        
        return dp[-1]




        
