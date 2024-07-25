class Solution(object):
    def maxProbability(self, n, edges, succProb, start_node, end_node):
        """
        :type n: int
        :type edges: List[List[int]]
        :type succProb: List[float]
        :type start_node: int
        :type end_node: int
        :rtype: float

        solution: 
         - dijkstra's with dist = success probability
         - uses max heap (min heap with negative values) => O(E * logV)
        """

        graph = [[] for _ in range(n)]

        for edge, prob in zip(edges, succProb):
            u, v = edge

            graph[u].append((v, prob))
            graph[v].append((u, prob))
        
        dist = [0.0] * n
        visited = [False] * n
        maxHeap = [(-1.0, start_node)]
        dist[start_node] = [1.0]

        while maxHeap:
            w, u = heapq.heappop(maxHeap)
            if visited[u]: continue
            visited[u] = True

            for v, c in graph[u]:
                if not visited[v] and c * (-w) > dist[v]:
                    dist[v] = c * (-w)
                    heapq.heappush(maxHeap, (c*w, v))
        
        return dist[end_node]





        
