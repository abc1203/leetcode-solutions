class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        idea:
         - constructs graph with curr = src & pre = tar; this allows dfs to append pre 1st
         - dfs(i): returns true if no cycle exists by starting in i
         - if no cycle exists, append i to ans
        """

        hm = {x:[] for x in range(numCourses)}
        for src, tar in prerequisites:
            hm[src].append(tar)
        
        ans = []
        visited, cycle = set(), set()

        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True

            cycle.add(crs)
            for tarCrs in hm[crs]:
                if dfs(tarCrs) == False: return False
            cycle.remove(crs)
            visited.add(crs)
            ans.append(crs)
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False: return []
        return ans

        
