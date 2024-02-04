class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = []
        l.append(0)
        l.append(1)
        for i in range(2, n+1):
            l.append(l[i-1]+l[i-2])
        return l[n]
      
