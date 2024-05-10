class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool

        idea: 
         - trees can't have cycles
         - run DFS & see if there are repeated visited nodes
         - only need to run DFS once because of the tree structure
         - here we use a global visited and keep track of parent => total O(n^2)
         - also checks if the graph is connected
        """

        visited = set()
        hmap = {x:[] for x in range(n)}

        for a, b in edges:
            hmap[a].append(b)
            hmap[b].append(a)
        
        # DFS
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for newNode in hmap[i]:
                if newNode != prev and not dfs(newNode, i): return False
            return True
        
        return dfs(0, -1) and (len(visited) == n)

        
        
        
