class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.

        idea:
         - approach 1: run bfs on each gate => TLE
        """
        m, n = len(rooms), len(rooms[0])

        def bfs(r, c):
            visited = set()
            d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            q = [(r, c, 0)]
            while q:
                (curr_r, curr_c, curr_dis) = q.pop(0)
                visited.add((curr_r, curr_c))
                
                for dr, dc in d:
                    new_r, new_c = curr_r + dr, curr_c + dc
                    
                    if new_r in range(m) and new_c in range(n) and \
                    (new_r, new_c) not in visited and rooms[new_r][new_c] > 0:
                        rooms[new_r][new_c] = min(rooms[new_r][new_c], curr_dis+1)
                        q.append((new_r, new_c, rooms[new_r][new_c]))
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: bfs(i, j)
                

        
