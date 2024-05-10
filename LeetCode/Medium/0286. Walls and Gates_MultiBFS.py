class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.

        idea:
         - approach 1: run bfs on each gate individually => n^2 * O(|V| + |E|) = O(n^4)
         - approach 2: run bfs on each gate at the same time => O(n^2)
        """
        m, n = len(rooms), len(rooms[0])
        q = []
        d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0: q.append((i, j, 0))
        
        while q:
            r, c, dis = q.pop(0)
            for dr, dc in d:
                nr, nc = r+dr, c+dc
                if nr in range(m) and nc in range(n) and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = dis + 1
                    q.append((nr, nc, rooms[nr][nc]))

                

        
