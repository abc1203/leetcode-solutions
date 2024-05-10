class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        idea:
         - sort start times
         - for each elem, if end[i] > start[i+1], 
            the interval becomes [start[i], max(end[i], end[i+1])]
        """

        intervals.sort()
        ans = []
        i, j = 0, 1

        while i < len(intervals):
            [start, end] = intervals[i]
            
            while j < len(intervals) and end >= intervals[j][0]:
                end = max(end, intervals[j][1])
                j += 1
            
            ans.append([start, end])
            i = j
            j += 1
        
        return ans
