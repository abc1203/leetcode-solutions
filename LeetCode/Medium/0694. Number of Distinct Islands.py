class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        idea:
         - record the directions of each island
         - since we always reach the top-left corner of each island first, tracking dir can identify
         - o origin, u/d/l/r dir, b back (necessary to track the exact steps)
        """
        ans = 0
        distinct = set()
        m,n = len(grid), len(grid[0])
        self.steps = ''

        def dfs(i, j, dir):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
                self.steps += dir
                grid[i][j] = 0

                dfs(i+1, j, 'd')
                dfs(i-1, j, 'u')
                dfs(i, j+1, 'r')
                dfs(i, j-1, 'l')
                self.steps += 'b'
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, 'o')
                    distinct.add(self.steps)
                    self.steps = ''
        # print(distinct)
        return len(distinct)

        
