class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        idea:
         - use hashmap to build adjacency list for graph
         - then the problem becomes if the graph is a tree (if cycle exists)
         - need to run dfs on all nodes to check if one path is possible
         - dfs: returns False if a cycle is detected in the subgraph with root curr
         - naively use dfs on all nodes TLE => del edges after checking node
        """

        hm = {x:[] for x in range(numCourses)}
        for i in range(len(prerequisites)):
            src, tar = (prerequisites[i])[0], (prerequisites[i])[1]
            hm[tar].append(src)
        
        visited = set()
        def dfs(curr):
            if curr in visited: return False
            if hm[curr] == []: return True

            visited.add(curr)
            for tar in hm[curr]:
                if not dfs(tar): return False
            visited.remove(curr)
            hm[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True
        
