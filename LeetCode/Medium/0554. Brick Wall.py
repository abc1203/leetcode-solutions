class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int

        approach:
         - have a hashmap for the number of crossed brickes for each number
         - hm[i] = number of edges at position i
        """

        hm = {0:0}
        for w in wall:
            s = 0
            for b in w[:-1]:
                s += b
                hm[s] = 1 + hm.get(s, 0)
        
        return len(wall) - max(hm.values())

        
