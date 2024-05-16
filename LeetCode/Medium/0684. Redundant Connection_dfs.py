class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]

        idea:
         - every time we add an edge, check if it creates a cycle by running dfs => O(N^2)
         - dfs: return True if there's a cycle
        """

        hm = {x:[] for x in range(1, len(edges)+1)}
        visited = set()

        def dfs(curr, prev):
            if curr in visited: return True

            visited.add(curr)
            for neigh in hm[curr]:
                if neigh != prev and dfs(neigh, curr): return True
            visited.remove(curr)
            return False

        for a, b in edges:
            if a not in hm: hm[a] = {b}
            else: hm[a].append(b)
            if b not in hm: hm[b] = {a}
            else: hm[b].append(a)
            
            if dfs(a, 0): return [a, b]   
        
        return -1
        

        
