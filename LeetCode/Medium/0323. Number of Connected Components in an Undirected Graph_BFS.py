class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int

        idea:
         - create a hashmap on the edges (key=src node, val= list of target nodes)
         - iterate each node; if they have non-zero deg, run BFS on it
         - constructing hmap: O(n^2), iterating: O(n^2)
        """

        hmap = {x:[] for x in range(n)}
        for a, b in edges:
            hmap[a].append(b)
            hmap[b].append(a)

        ans = 0
        # efficient BFS implementation
        for i in range(n):
            q = [i]
            ans += 1 if i in hmap else 0
            for j in q:
                if j in hmap:
                    q += hmap[j]
                    del hmap[j]
        
        return ans


        

        
