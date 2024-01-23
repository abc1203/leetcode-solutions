class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int

        idea: 
        use binary search with l = 1 & r = max(pile)
        define mid = (l+r)/2; apply binary search by checking if mid works
        checking takes O(n) => O(nlogn) total
        if it works, make r = mid-1 & update ans
        if it doesn't work, make l = mid + 1
        """

        l, r = 1, max(piles)
        ans = r
        while l <= r:
            mid = (l + r) / 2

            # check if mid works
            hrs = 0
            for i in range(len(piles)):
                hrs += (piles[i] / mid) + (1 if piles[i] % mid > 0 else 0)
            
            if hrs <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return ans



        
