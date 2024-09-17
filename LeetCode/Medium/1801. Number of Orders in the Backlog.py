class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int

         - use heaps
        """

        buy_log, sell_log = [], []

        for order in orders:
            curr_qty = order[1]

            if order[2] == 0: # buy
                while curr_qty > 0 and len(sell_log) > 0 and order[0] >= sell_log[0][0]:
                    if curr_qty >= sell_log[0][1]:
                        curr_qty -= sell_log[0][1]
                        heapq.heappop(sell_log)
                    else:
                        sell_log[0][1] -= curr_qty
                        curr_qty = 0
                
                if curr_qty > 0: heapq.heappush(buy_log, [-order[0], curr_qty])
            else: # sell
                while curr_qty > 0 and len(buy_log) > 0 and order[0] <= -buy_log[0][0]:
                    if curr_qty >= buy_log[0][1]:
                        curr_qty -= buy_log[0][1]
                        heapq.heappop(buy_log)
                    else:
                        buy_log[0][1] -= curr_qty
                        curr_qty = 0
                
                if curr_qty > 0: heapq.heappush(sell_log, [order[0], curr_qty])
        
        ans = 0
        for item in buy_log: ans += item[1]
        for item in sell_log: ans += item[1]
        return ans % (10**9+7)


        
