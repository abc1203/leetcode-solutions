class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        while l <= r:
            m = (l+r)/2
            res = m * m
            if res <= x and (m+1) * (m+1) > x: return m
            elif res < x: l = m + 1
            else: r = m-1
        return -1
