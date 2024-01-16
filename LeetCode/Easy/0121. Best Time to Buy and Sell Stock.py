class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        algo:
        1. keep track of the current lowest price and iterate
        2. find the profit for today's price - lowest price
        """

        max_profit = 0
        lowest_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
            
            max_profit = max(max_profit, prices[i] - lowest_price)
        
        return max_profit
        
