class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        idea:
         - run bfs
        """

        ans = 0
        visited = set()

        def bfs(row, col):
            area = 1
            visited.add((row, col))
            q = [(row, col)]

            while q:
                (r, c) = q.pop(0)
                dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

                for dr, dc in dirs:
                    new_r, new_c = r+dr, c+dc

                    if new_r in range(len(grid)) and new_c in range(len(grid[0])) and \
                        grid[new_r][new_c] == 1 and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))
                        q.append((new_r, new_c))
                        area += 1

            return area
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    ans = max(ans, bfs(r, c))
        
        return ans

            



        
