class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        idea:
         - run bfs
        """
        ans = 0
        visited = set()
        q = []
        r_len, c_len = len(grid), len(grid[0])

        def bfs():
            while len(q) != 0:
                (r, c) = q.pop(0)

                dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in dir:
                    new_r, new_c = r+dr, c+dc
                    if new_r in range(r_len) and \
                        new_c in range(c_len) and \
                        grid[new_r][new_c] == "1" and \
                        (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))
                        
        
        for i in range(r_len):
            for j in range(c_len):
                if grid[i][j] == "1" and (i, j) not in visited:
                    ans += 1
                    q.append((i, j))
                    bfs()

        return ans

        
