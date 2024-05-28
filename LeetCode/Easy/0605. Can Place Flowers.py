class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool

        approach:
         - when encountered a 0, continue iterating until reach a 1
         - when encountered a 1, round down on the (reached slots/2) and reset
        """

        
        # handle 0 0 ... 0
        empty = 0 if flowerbed[0]==1 else 1
        for f in flowerbed:
            # cases 1 0 ... 0 1 or 0 ... 0 1
            if f and empty > 0:
               n -= int((empty-1) / 2)  # int division, round toward zero
               empty = 0
            elif not f:
               empty += 1
            print(empty)

        # cases 1 0 0 0...
        if empty > 0: n -= int(empty/2)
        return n <= 0
        
