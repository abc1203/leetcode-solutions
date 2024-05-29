class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        idea:
         - track the lowest
         - when prices[i+1] < price[i], sell it from lowest price and reset
        """

        lowest = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i-1]:
                ans += (prices[i-1] - lowest)
                lowest = prices[i]
            lowest = min(lowest, prices[i])
        
        return ans + (prices[len(prices)-1] - lowest)


        
