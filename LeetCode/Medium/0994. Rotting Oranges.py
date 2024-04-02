class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        idea:
         - simulate what happens similar to bfs
        """

        time = 0
        num_fresh = 0
        q = []

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1: num_fresh += 1
                if grid[r][c] == 2: q.append((r, c))
        
        while num_fresh > 0 and q:
            new_q = []
            for (r, c) in q:
                for dr, dc in dirs:
                    new_r, new_c = r+dr, c+dc

                    if new_r in range(len(grid)) and new_c in range(len(grid[0])) and \
                    grid[new_r][new_c] == 1 and (new_r, new_c) not in q:
                        grid[new_r][new_c] = 2
                        new_q.append((new_r, new_c))
                        num_fresh -= 1

            q = new_q
            time += 1
        
        if num_fresh > 0: return -1
        return time
        


        
